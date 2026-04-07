# Mini ETL data pipeline project

## 1. Project Description
- Mini ETL data pipeline project는 여러 개의 CSV 파일을 읽어 데이터를 정제하고, 가공된 데이터를 SQLite 데이터베이스에 저장합니다.

## 2. Purpose
- 이 프로젝트는 Data Engineer의 기본기와 데이터 파이프라인의 핵심 구조인 ETL(Extract, Transform, Load) 과정을 직접 구현하며, 데이터 수집, 정제, 저장의 흐름을 이해하기 위해 진행하였습니다.

## 3. Tech Stack
- Language: Python
- Libraries: Pandas
- Database: SQLite
- IDE: Visual Studio Code

## 4. File Structure
- data
    - students1.csv
    - students2.csv
- database
    - students.db
- output
    - invalid.txt
- main.py
- README.md

## 5. Features
- 여러 개의 CSV 파일을 자동으로 읽어오는 기능
- 유효하지 않은 데이터를 식별하고 별도로 저장하는 기능
- 문자형 성적('A', 'B', 'C', 'D')을 숫자로 변환하는 기능
- 기준 점수 이상의 데이터만 필터링하는 기능
- 정제된 데이터를 SQLite 데이터베이스에 저장하는 기능

## 6. How to Run
1. 필요한 라이브러리 설치
   pip install pandas
2. data/ 폴더에 CSV 파일을 준비합니다.
3. 아래 명령어로 프로그램을 실행합니다.
   python main.py


## 7. Example Data

### Input Data (CSV)

| name  | grade |
|-------|-------|
| John  | A     |
| Mike  | X     |
| Sara  | B     |

### Invalid Data (output/invalid.txt)

| name  | grade |
|-------|-------|
| Mike  | X     |