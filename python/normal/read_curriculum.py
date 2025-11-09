import pandas as pd
import sys
import io

# UTF-8 출력 설정
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 엑셀 파일 읽기
file_path = r'C:\Users\User\Downloads\교과편성+연계표.xlsx'

try:
    # 모든 시트 확인
    excel_file = pd.ExcelFile(file_path)
    print("시트 목록:", excel_file.sheet_names)
    print("\n" + "="*80)

    # 각 시트 읽기
    for sheet_name in excel_file.sheet_names:
        print(f"\n시트: {sheet_name}")
        print("-"*80)
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(df.to_string())
        print(f"\nshape: {df.shape} (행: {df.shape[0]}, 열: {df.shape[1]})")
        print(f"컬럼: {df.columns.tolist()}")
        print("="*80)

except Exception as e:
    print(f"에러 발생: {e}")
    import traceback
    traceback.print_exc()
