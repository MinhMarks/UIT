import pandas as pd
import os

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def generate_latex_tables(csv_file, output_dir="latex_tables"):
    # Đọc file CSV
    df = pd.read_csv(csv_file)

    # Tạo thư mục lưu bảng nếu chưa có
    os.makedirs(output_dir, exist_ok=True)

    # Danh sách các group
    groups = df['Group'].unique()

    for group in groups:
        group_df = df[df['Group'] == group].copy()
        group_df = group_df.sort_values(by="File")

        # Chuyển đổi cột is_optimal thành ký hiệu
        group_df["Optimal"] = group_df["is_Optimal"].apply(
            lambda x: r"\checkmark" if x else r"$\times$"
        )

        # Sinh LaTeX table
        latex = []
        latex.append(r"\begin{table}[h!]")
        latex.append(r"\centering")
        latex.append(fr"\caption{{Kết quả thực nghiệm trên nhóm \texttt{{{group}}}. Giá trị lời giải là tổng giá trị của các vật phẩm được chọn, Tổng trọng lượng được tính tương ứng. Ký hiệu ``\checkmark'' nếu lời giải trả về là tối ưu, ``$\times$'' trong trường hợp ngược lại.}}")
        latex.append(r"\begin{tabular}{|c|c|c|c|}")
        latex.append(r"\hline")
        latex.append(r"\textbf{Test Case} & \textbf{Giá trị lời giải} & \textbf{Tổng trọng lượng} & \textbf{Lời giải tối ưu} \\")
        latex.append(r"\hline")

        for _, row in group_df.iterrows():
            test_case = row["File"]
            val = f"{row['Total_Value']:.3f}"
            wt = f"{row['Total_Weight']:.3f}"
            opt = row["Optimal"]
            latex.append(fr"{test_case} & {val} & {wt} & {opt} \\")
        
        latex.append(r"\hline")
        latex.append(r"\end{tabular}")
        latex.append(r"\end{table}")

        latex_code = "\n".join(latex)

        # Lưu ra file .tex
        tex_filename = os.path.join(output_dir, f"aggregate.tex")
        with open(tex_filename, "a", encoding="utf-8") as f:
            f.write(latex_code)

        print(f" Đã sinh bảng LaTeX cho nhóm {group}: {tex_filename}")

# Gọi hàm
if __name__ == "__main__":
    generate_latex_tables("1minute_knapsack_results.csv")
