import os
import csv
from ortools.algorithms.python import knapsack_solver

BASE_DIR = "kplib"  # thư mục gốc chứa các nhóm test

# Đọc file knapsack (giả định định dạng chuẩn từ kplib)
def read_knapsack_file(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    n_items = int(lines[0])
    capacities = [int(lines[1])]
    values = []
    weights = []

    for line in lines[2:2 + n_items]:
        value, weight = map(int, line.split())
        values.append(value)
        weights.append(weight)

    return values, [weights], capacities

# Giải bài toán knapsack dùng OR-Tools
def solve_knapsack(values, weights, capacities):
    solver = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackSolver"
    )
    
    solver.init(values, weights, capacities)
    solver.set_time_limit(60) 
    total_value = solver.solve()

    packed_items = []
    total_weight = 0

    for i in range(len(values)):
        if solver.best_solution_contains(i):
            packed_items.append(i)
            total_weight += weights[0][i]

    return total_value, total_weight, packed_items, solver.is_solution_optimal()


# Lặp qua 13 nhóm thư mục
def main():
    base_path = "kplib"  
    groups = [
        "00Uncorrelated", "01WeaklyCorrelated", "02StronglyCorrelated", "03InverseStronglyCorrelated",
        "04AlmostStronglyCorrelated", "05SubsetSum", "06UncorrelatedWithSimilarWeights", "07SpannerUncorrelated",
        "08SpannerWeaklyCorrelated", "09SpannerStronglyCorrelated", "10MultipleStronglyCorrelated",
        "11ProfitCeiling", "12Circle"
    ]
    group_paths = [os.path.join(base_path, group) for group in groups]

    # Ghi kết quả vào file CSV
    with open("1minute_knapsack_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Group", "File", "Total_Value", "Total_Weight", "Num_Items", "is_Optimal"])

        for group in group_paths:
            previous = 0 
            state = 0 
            for root, _, files in os.walk(group):
                state = state + 1 
                if previous == root or state % 2 == 0:
                    continue 
                previous = root 
                count = 0
                for file in sorted(files):
                    print(f"Processing {file} in {root}...") 
                    if file.endswith((".kp", ".txt", ".dat")):
                        try:
                            file_path = os.path.join(root, file)
                            values, weights, capacities = read_knapsack_file(file_path)
                            total_value, total_weight, packed_items, is_optimal = solve_knapsack(values, weights, capacities)

                            writer.writerow([
                                root.split("\\")[1],  # Nhóm
                                root.split("\\")[2],  # Nhóm
                                total_value,
                                total_weight,
                                len(packed_items), 
                                is_optimal
                            ])

                            count += 1
                            if count >= 1:
                                break
                        except Exception as e:
                            print(f"❌ Error in file {file_path}: {e}")
                    break 

if __name__ == "__main__":
    main()
