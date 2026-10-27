---
layout: default
title: Portfolio
---

# DevOps Engineer

AWS·Kubernetes 환경에서 개발자의 반복 작업을 자동화하고, 인프라 변경을 안전하게 수행할 수 있는 플랫폼과 운영 체계를 구축해 왔습니다. 서비스 개발 경험을 바탕으로 개발자의 불편을 파악하고, 셀프서비스 도구와 공통 운영 설정으로 개선하는 데 집중합니다.

<div id="experience"></div>
## 경력사항

### 씨제이올리브영주식회사

- 기간: 2025.09 - 2026.09
- 직무: DevOps / 인턴
- Backstage 기반 서비스 생성·배포 자동화 및 개발 도구 통합
- Terraform·Terragrunt 기반 EKS 네트워크 구성 변경 및 서비스 마이그레이션
- PR 기반 인프라 변경 통제 및 Drift 탐지 자동화
- Istio 장애 분석, CI 빌드 성능 개선 및 인프라 비용 최적화

### 주식회사스노우온카드

- 기간: 2024.12 - 2025.09
- 직무: 서버개발 / 대리
- Spring 기반 토큰 결제 및 PG 간편결제 연동 API 개발
- DB 스키마 재설계·데이터 마이그레이션 및 React 기반 운영 어드민 개발

<div id="projects"></div>
## 대표 경험

### 씨제이올리브영주식회사

#### 내부 개발자 플랫폼(IDP) 구축

- 기간: 2025.09 - 2026.02
- 역할: Backstage 코어 플러그인 외 IDP 기능 개발 및 플랫폼 통합
- 조직·관리 대상 규모: 약 100명 규모 조직, 당시 Repository 70개 이상
- 기술: Backstage, React, Node.js, TypeScript, Kubernetes, Helm, Argo CD

##### 문제와 선택 근거

기존 Port.io 기반 포털은 조직 요구사항에 맞춘 기능 확장에 한계가 있었습니다. 개발자가 Kubernetes 매니페스트를 이해하고 GitOps Repository에 배포 PR을 올리기까지 최소 하루가 필요했습니다. 조직별 기능 확장이 필요해, 플러그인 생태계가 활발한 Backstage를 선택하고 기존 포털을 대체했습니다.

##### 구현

- Scaffolder Template과 공통 베이스 Repository를 활용해 Repository 생성, Kubernetes Values 및 Argo CD 배포 설정 생성을 자동화
- 기존 Repository를 Backstage Catalog로 마이그레이션해 서비스 메타데이터 통합 관리
- Argo CD, k6 Operator, Spring Batch를 Plugin으로 통합해 배포·성능 테스트·배치 관리 기능 제공

##### 결과

- 신규 서비스 생성부터 배포까지 약 5분 소요
- Repository 생성 경로를 Backstage로 일원화해 초기 설정 표준화
- 여러 운영 도구에 분산된 작업을 하나의 포털에서 수행하도록 개선

#### EKS 신규 클러스터 구축 및 서비스 마이그레이션

- 기간: 2026.04
- 역할: 기존 IaC 수정, 신규 클러스터 구축·네트워크 검증 및 서비스 전환
- 대상: Dev 전용 클러스터 1개와 Stg·Prd 공유 클러스터 1개의 서비스 이전
- 기술: Terraform, Terragrunt, EKS, Amazon VPC CNI, Cilium, ExternalDNS, Route53, Datadog

##### 문제와 선택 근거

기존 Cilium의 `tunnel: vxlan` 기반 Overlay에서는 Pod가 RDS 등 VPC 내부 리소스에 접근할 때 노드 IP를 통한 SNAT이 필요했습니다. Pod에 VPC Secondary CIDR 대역의 IP를 할당해 직접 라우팅이 가능한 구조로 전환하고, SNAT 의존성과 네트워크 복잡성을 줄이고자 했습니다.

CNI 변경의 영향을 운영 환경에서 분리하기 위해 팀에서 신규 클러스터 구축 후 점진적 이전을 결정했습니다. 주요 구성요소가 GitOps로 관리되어 신규 환경을 빠르게 재현할 수 있었습니다.

##### 구현

- 기존 Terraform 모듈·Terragrunt 구성을 수정하고 Amazon VPC CNI Managed Add-on과 Cilium chaining으로 신규 클러스터 구성
- 기존·신규 클러스터의 NLB를 동일 도메인에 등록하고, HTTPRoute의 ExternalDNS annotation 변경을 ExternalDNS가 Route53 Weighted Routing에 반영하도록 구성
- Dev·Stg·Prd 서비스 이전과 가중치 조정을 통한 트래픽 전환 직접 수행

##### 검증과 롤백 계획

- Pod IP 할당과 CNI의 SNAT·Masquerading 설정을 점검하고, VPC Flow Logs에서 RDS 방향 트래픽의 Source IP가 Pod IP와 일치하는지 확인
- 실제 API 트래픽을 점진적으로 유입하며 Datadog의 요청량·응답 시간·오류율을 기존 환경과 비교하고, APM으로 DB 연결 오류·지연 여부 확인
- 특이사항이 없으면 트래픽을 확대하고, 문제 발생 시 유지 중인 기존 클러스터로 Route53 가중치를 되돌리도록 계획

##### 결과

- Dev·Stg·Prd 서비스 이전을 완료했으며, 전환 중 특이사항이 없어 실제 롤백은 수행하지 않음
- 검증한 Pod → RDS 통신에서 노드 IP로 SNAT되지 않고 Pod IP가 유지됨을 확인

#### Istio Ambient 간헐적 503 분석 및 Connection 정책 개선

- 기간: 2026.08
- 역할: 간헐적 503 분석, Connection 재사용 정책 조정 및 Base Chart 공통 설정 구현
- 기술: Istio Ambient, Waypoint, Envoy, DestinationRule, Spring Boot, Embedded Tomcat, Datadog

##### 문제와 분석 근거

Production 환경의 서비스 간 호출에서 간헐적 HTTP 503 오류가 발생했습니다. Waypoint Envoy Access Log의 `upstream_reset_before_response_started` 등 연결 종료 관련 오류와 Tomcat의 Keep-Alive 설정을 비교했습니다. Tomcat이 종료한 Connection을 Envoy가 재사용하는 과정의 Race Condition을 원인 가설로 두고 정책을 조정했습니다.

##### 조치와 검증

- DestinationRule에 `idleTimeout`과 `maxRequestsPerConnection: 90`을 적용해 Upstream Connection 재사용 정책 조정
- Datadog에서 해당 서비스의 오류율·응답 상태를 모니터링하고 Waypoint의 연결 관련 오류 재발 여부를 확인하는 방식으로 검증
- Base Chart에 DestinationRule 템플릿과 Values Override 기능을 추가해 다른 서비스에도 공통 방식으로 정책을 적용할 수 있도록 구성

## 추가 운영 개선

### 공유 인프라의 변경 충돌 방지 및 구성 일관성 검증 자동화

- 기술: Terraform, Digger, GitHub Actions, ARC, Kubernetes
- 여러 개발자가 공유하는 Terraform 인프라에 기존 ARC 기반 Self-hosted Runner를 활용한 PR 기반 Plan/Apply 절차 구축
- Apply 실행 권한을 통제하고 Terraform State Lock·PR 단위 Lock으로 동시 실행 및 변경 충돌 위험 제어
- 정기 Plan 실행으로 IaC 코드와 실제 AWS 리소스 간 Drift를 지속적으로 탐지
- 변경 이력과 실행 결과를 PR에 기록해 인프라 변경의 추적성 확보

### Gradle 빌드 캐시 최적화

- 기간: 2026.05 / 기술: GitHub Actions ARC, Kubernetes, S3, EFS, Gradle
- 공용 EFS 경로에 누적된 Gradle 캐시의 I/O 병목과 관리 부담을 줄이기 위해 Repository별 S3 경로로 캐시 저장 구조 전환
- Runner Hook으로 Job 시작·종료 시 캐시 복원·저장을 자동화하여 서비스별 Workflow 수정 없이 공통 정책 적용
- Gradle 빌드 시간 약 39% 단축 및 EFS I/O 병목 완화

### ECR Multi-Region 및 비용 최적화

- 기간: 2026.07 / 기술: Amazon ECR, ECR Pull Through Cache, ECR Lifecycle Policy
- Virginia EKS에서 Seoul ECR 이미지를 가져오는 구조를 개선하기 위해 Virginia 리전에 Pull Through Cache 구성
- 운영 배포 이미지에 `prd-YYYYMMDD-commitHash` 태그를 추가하고, 운영 배포 이미지를 제외한 30일 이상 경과 이미지의 자동 삭제 정책 적용
- 운영 배포·롤백 이력을 보호하면서 ECR 월 비용 약 $300 → $200으로 약 33% 절감

### 오픈소스 기반 Incident Management 시스템 내제화

- 기간: 2026.05 / 기술: OneUptime, On-Call, Alerting, Slack
- PagerDuty 라이선스 비용 부담에 대응해 On-Call·Escalation·Alert 연계 기능을 비교·검증하고 OneUptime을 신규 프로젝트에 적용
- Alert Severity에 따른 담당자 호출·Incident 생성과 Slack 전용 채널 생성·관련자 초대를 자동화
- 담당자 알림부터 협업까지 이어지는 장애 대응 절차 표준화

### EKS 환경에 NodeLocal DNS 도입

- 기간: 2026.04 / 기술: EKS, CoreDNS, NodeLocal DNSCache
- CoreDNS 업데이트·장애 시 DNS 응답 영향을 완화하기 위해 Node 단위 DNS Cache 및 Proxy 구성
- 캐시된 DNS 레코드의 요청을 Node에서 처리하여 CoreDNS 의존도와 부하 완화

<div id="oss"></div>
## 오픈소스 기여

### Argo CD: <a href="https://github.com/argoproj/argo-cd/pull/25590" target="_blank" rel="noreferrer noopener">argoproj/argo-cd#25590</a>

약 70개 서비스의 Application 설정 변경 과정에서 개별 탐색의 비효율을 발견했습니다. Issue를 등록하고 Dashboard의 annotation 기반 조회 기능을 구현했습니다.

### Backstage Plugin: <a href="https://github.com/backstage/backstage/pull/32216" target="_blank" rel="noreferrer noopener">backstage/backstage#32216</a>

서비스 단위 DORA Metrics 시각화 플러그인을 개발해 Backstage Plugin Marketplace에 배포했습니다. 주당 약 50~100회 다운로드가 발생하며, 사용자 Issue·PR을 바탕으로 개선·유지보수하고 있습니다.

### Terrateam: <a href="https://github.com/terrateamio/terrateam/pull/1058" target="_blank" rel="noreferrer noopener">terrateamio/terrateam#1058</a>

사용 중 발견한 UI 이슈를 재현하고 수정했습니다.

## 기술 스택

- Infra / DevOps: AWS, Kubernetes, Istio Ambient, Helm, Argo CD, Terraform, GitHub Actions ARC
- Platform / 개발: Backstage, Node.js, TypeScript, React, Go, Spring
- DB: MySQL, Oracle, PostgreSQL

<div id="certs"></div>
## 자격증

- AWS Certified Solutions Architect - Associate (SAA) / 2026.02 / AWS
- 리눅스마스터 2급 / 2024.09 / 한국정보통신인력개발센터
- 정보처리기사 / 2024.09 / 한국산업인력공단
- SQL개발자(SQLD) / 2024.06 / 한국데이터베이스진흥센터

<div id="education"></div>
## 학력

### 인하대학교

- 2014.03 - 2021.02 (졸업)
- 항공우주공학과 학사
