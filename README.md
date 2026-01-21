# Encrypted-Stock-Portfolio
  **TenSEAL(CKKS) 동형암호를 활용한 프라이버시 보존형 주식 포트폴리오 분석 시스템**

본 프로젝트는 사용자의 민감한 금융 데이터를 암호화된 상태에서 복호화하지 않고도, 서버에서 실시간 시장 데이터를 결합하여 수익률 및 리스크를 분석할 수 있는 보안 특화 금융 분석 엔진을 구현한다.

---
### Feature

- Private-Preserving Analystics: 동형암호(CKKS 알고리즘)를 사용하여 사용자의 자산 정보를 서버에 노출 없이 처리

- Real-time Market integration: ``` FinanceDataReader ``` API를 활용하여 KOSPI 상위 100개 종목의 실시간 시세 및 거래량 데이터 반영

- Scalable Data Simulation: 100명의 가상 사용자에 대한 포트폴리오(총 1000행)를 생성하여 데이터 처리 능력 및 정확도 검증
---
### Tech Stack
Language: Python

Encryption: TenSEAL (Homomorphic Encryption)

Data Analysis: Pandas, NumPy

Financial Data: FinanceDataReader, Yahoo Finance

----
### Dataset Details
1) Source: 한국거래소(KRX) 시가총액 상위 100대 기업

2) Fields: Purchase_Price(암호화 대상), Quantity(암호화 대상), Current_Price, Trading_Volume, Volatility
