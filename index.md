---
layout: default
title: Portfolio
---

# Portfolio

## 핵심 역량

서비스를 개발하고 운영하는 과정에서 반복되는 불편함을 발견하면, 원인을 구조적으로 분석해 자동화와 표준화로 해결하는 엔지니어입니다. 내부 플랫폼 구축을 통해 서비스 셋업 시간을 1일에서 10분으로 단축하고 운영 가시성을 높였으며, 현업에서 마주한 문제를 오픈소스 기여로 연결해 실제 사용자 경험 개선까지 확장해왔습니다.

## 기술 스택

- Backend: Spring, Node.js, Go
- Frontend: React, TypeScript
- Infra/DevOps: Kubernetes, Helm, Argo CD, AWS
- DB: MySQL, Oracle, PostgreSQL

## Open Source Contributions

### argo-cd: <a href="https://github.com/argoproj/argo-cd/pull/25590" target="_blank" rel="noreferrer noopener">argoproj/argo-cd#25590</a>

Argo CD 파이프라인 개선 과정에서 약 70여 개 서비스의 Application 설정을 수정해야 했으나, Dashboard에서 annotation 기반 조회 기능이 없어 각 Application을 개별적으로 탐색해야 하는 비효율이 발생했습니다.

문제를 해결하기 위해 Argo CD 저장소에 Issue를 등록하고 annotation 기반 조회 기능을 구현하여 프로젝트에 기여했습니다.

### Backstage Plugin: <a href="https://github.com/backstage/backstage/pull/32216" target="_blank" rel="noreferrer noopener">backstage/backstage#32216</a>

Backstage 기반 IDP 구축 과정에서 서비스 단위 DORA Metrics 시각화 플러그인을 개발하고 Backstage Plugin Marketplace에 배포했습니다.

주당 약 50~100회 다운로드가 발생하며 실제 사용자들이 활용 중이고, 사용자 Issue 및 PR이 이어지면서 Backstage 생태계에 기여했습니다. 이를 기반으로 지속적인 기능 개선 및 유지보수를 진행하고 있습니다.

### terrateam: <a href="https://github.com/terrateamio/terrateam/pull/1058" target="_blank" rel="noreferrer noopener">terrateamio/terrateam#1058</a>

Terrateam 사용 중 발견한 UI 이슈를 재현하고 수정한 기여입니다. 기능 확장보다는 사용자 경험을 개선하는 버그 수정 성격의 PR입니다.

## 경력사항

### 씨제이올리브영주식회사

- 기간: 2025.09 - 2026.03 (6개월)
- 직무: DevOps
- 주요 프로젝트: [개발자 내부 플랫폼(IDP) 구축](#개발자-내부-플랫폼idp-구축)

### 주식회사스노우온카드

- 기간: 2024.12 - 2025.09 (10개월)
- 직무: 서버개발
- 직급: 대리
- 주요 프로젝트:
  - [Token 기반 비접촉 결제 솔루션 구축 (HCE / Scan to Pay)](#token-기반-비접촉-결제-솔루션-구축-hce--scan-to-pay)
  - [간편결제 통합 인터페이스 구축(SI)](#간편결제-통합-인터페이스-구축si)

## 프로젝트

### 개발자 내부 플랫폼(IDP) 구축

- 기간: 2025.09 - 2026.01
- 직무: DevOps
- 기술스택: React, Node.js, TypeScript, Kubernetes, Helm, Argo CD, AWS

### 1. 프로젝트 배경

- 100여 개 서비스가 팀별로 상이한 생성·배포·운영 방식을 사용하여 표준화 수준이 낮고, 신규 서비스 셋업에 평균 1~2일 소요
- 개발~배포~운영~문서를 통합 관리할 수 있는 플랫폼 부재로 DevEx 저하

### 2. 주요 업무 및 성과

#### 1) 스캐폴딩 템플릿 개발

- CI/CD, Helm, Argo CD 설정 자동 생성 템플릿 설계
- 신규 서비스 셋업 1일 → 10분 (90% 단축)
- 표준 배포 구조 정립

#### 2) 서비스 카탈로그 구축

- 저장소·CI/CD·배포·모니터링·문서 통합 조회 체계 구축
- 약 100개 서비스 등록 및 운영 가시성 확보

#### 3) DORA Metrics 대시보드 구현

- Deployment Frequency, Lead Time, CFR, MTTR 자동 집계·시각화
- 정량 지표 기반 개선 루프 정착

#### 4) Cost Insights 구축

- AWS CUR 기반 일 단위 비용 집계 파이프라인 설계
- 리소스 단위 비용 분해 및 스파이크 탐지 체계 구축
- 비용 원인 분석 시간 단축 및 FinOps 의사결정 개선

### Token 기반 비접촉 결제 솔루션 구축 (HCE / Scan to Pay)

- 기간: 2025.06 - 2025.07
- 직무: 서버개발
- 기술스택: Spring, MySQL
- 설명: Visa, Mastercard 등 국제 브랜드의 토큰 기반 결제 프로세스를 구현하고, HCE 및 QR 기반 Scan to Pay 기능을 포함한 TLCM 솔루션 개발

#### 주요 업무 및 성과

- EMVCo 기반 Visa / Mastercard 결제 흐름 분석 및 토큰화 프로세스 구현 (Provisioning, Payment, Lifecycle 관리)
- Spring 기반 백엔드 모듈 설계 및 구현 (TSP 연동, HCE 카드 생성, QR 결제 요청 처리 등)
- 카드사 및 브랜드사 요구사항에 맞춘 TLCM (Transaction Life Cycle Management) 기능 구현
- 테스트 시뮬레이션 환경 구축 (APDU 커맨드/응답 처리)

### 간편결제 통합 인터페이스 구축(SI)

- 기간: 2025.02 - 2025.05
- 직무: 서버개발
- 기술스택: React, TypeScript, Spring, Oracle
- 설명: PG사 간편결제 등록·승인·취소 API를 통합 관리하는 백엔드 인터페이스와 어드민 시스템 구축

#### 주요 업무 및 성과

- 주요 PG사 간편결제 연동 API 설계 및 구현 (Spring 기반 서버 개발)
- TO-BE 정규화 DB 스키마 재설계 및 데이터 마이그레이션
- React 기반 어드민 대시보드 개발 (결제 통계: 건수, 승인 실패율 등 실시간 시각화)

## 자격증

### 리눅스마스터 2급

- 2024.09 / 한국정보통신인력개발센터

### 정보처리기사

- 2024.09 / 한국산업인력공단

### SQL개발자(SQLD)

- 2024.06 / 한국데이터베이스진흥센터

### AWS Certified Solutions Architect - Associate (SAA)

- 2026.02 / AWS

## 어학

### TOEIC Speaking Test

- 130점 (2024.07.01)

## 학력

### 인하대학교

- 2014.03 - 2021.02
- 항공우주공학
