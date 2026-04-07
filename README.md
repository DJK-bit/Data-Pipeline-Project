# Mini ETL Data Pipeline Project

## 1. Project Description
- Mini ETL data pipeline project는 여러 개의 CSV 파일을 읽어 데이터를 정제하고, 가공된 데이터를 SQLite 데이터베이스에 저장 및 조회합니다.

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

## 5. Workflow 
1. data/ 폴더 내 CSV 파일을 자동으로 탐색 및 로드  
2. Pandas를 사용하여 여러 파일을 하나의 데이터프레임으로 병합  
3. 유효하지 않은 데이터(grade 값이 A~D가 아닌 경우)를 output/invalid.txt로 분리 및 저장  
4. 문자형 성적(A, B, C, D)을 숫자형으로 변환  
5. 특정 조건(성적이 B 이상)에 따라 데이터 필터링  
6. 정제된 데이터를 SQLite 데이터베이스에 저장 및 조회   

## 6. Features 
- 다수 CSV 파일 자동 수집 (Data Ingestion)  
- 데이터 검증 및 오류 데이터 로깅 (Data Validation)  
- 데이터 변환 (Data Transformation)  
- 조건 기반 데이터 필터링  
- SQLite를 활용한 데이터 저장 (Data Loading)  

## 7. How to Run
1. 필요한 라이브러리 설치
   pip install pandas
2. data/ 폴더에 CSV 파일을 준비합니다.
3. 아래 명령어로 프로그램을 실행합니다.
   python main.py

## 8. Example Data

### Input Data (CSV)

| name  | grade |
|-------|-------|
| John  | A     |
| Mike  | X     |
| Sara  | B     |
| David | A     |
| Josh  | B     |
| Tom   | A     |
| Sarah | B     |

### Invalid Data (output/invalid.txt)

| name  | grade |
|-------|-------|
| Mike  | X     |

## Future improvements
- Flask를 활용한 API 형태로 확장   
- 대용량 데이터 처리를 위한 Spark 학습 및 적용  
