# Ruhulla Sheik

**Senior Software Engineer · AI Platform Engineer · Integration Engineer**

sk.ruhulla@gmail.com | +91 9035786999 | linkedin.com/in/ruhullasheik | github.com/ruhullasheik | Bangalore, India

## Professional Summary

Engineer who takes initiative, steps up to lead, and picks up new technology fast. **12+ years at a single company across three acquisitions** — progressing from Integration Engineer owning full customer-facing ERP projects solo, to Software Developer building core platform products, to Senior Engineer architecting production AI infrastructure. Most recently built a production **MCP (Model Context Protocol) AI gateway serving 20,000+ API calls/day** and shipped a conversational AI agent using Langflow and Azure OpenAI. Equally comfortable deep in code or leading a team — depending on what the project needs.

## Technical Skills

**Languages:** C#, Python, Java, TypeScript, PowerShell, SQL<br>
**AI & MCP:** Model Context Protocol (MCP), Langflow, Azure OpenAI, FastMCP, Claude Code, Spec-Driven Development<br>
**Frameworks:** ASP.NET Core, FastAPI, Apache Airflow, Quarkus, Vue 3 / Vite, Entity Framework Core, IdentityServer4<br>
**Cloud & Infra:** Azure (AKS, Bicep, Pipelines, Service Bus, Key Vault, App Insights, Redis Cache, Load Test, Logic Apps, ADF), Docker, Kubernetes, Helm<br>
**Databases:** PostgreSQL, SQL Server / Azure SQL, MongoDB / Cosmos DB<br>
**Auth & Security:** OAuth2, OIDC, SAML 2.0, JWT / JWKS, IdentityServer4, Bandit (SAST), pip-audit (SCA), Ory Keto (Google Zanzibar)<br>
**Observability:** OpenTelemetry, Grafana, Loki, Azure Application Insights<br>
**Messaging:** Apache Kafka, Azure Service Bus, RabbitMQ<br>
**Testing:** pytest, xUnit, Vitest, JUnit, JMeter, FakeItEasy<br>
**Integration & ERP Templates:** SAP (JCo, HANA), Oracle EBS, JD Edwards

## Professional Experience

### Logility Solutions, an Aptean Company *(formerly AdapChain Solutions)* — Bangalore, India | Mar 2014 – Present

#### Senior Software Engineer — Platform AI Enablement · Mar 2024 – Present

**MCP Gateway** · Jan 2026 – May 2026 · `Python` `FastMCP` `FastAPI` `PostgreSQL` `Redis` `OpenTelemetry` `AKS`

- **Architected and shipped** a production AI gateway **serving 20,000+ API calls/day** across a multi-tenant Azure platform — auto-discovers OpenAPI specs and exposes them as MCP tools. **Tech Lead**, lead contributor, and sole mandatory PR reviewer.
- Designed **instance-aware multi-tenant URL resolution** so a single deployed gateway serves all tenants with isolated, per-tenant backend routing — eliminating per-tenant deployments. MCP tools resolve backend URLs at runtime via the Client Catalog service.
- Built the full identity plumbing: **IAM-to-IDG token translation**, a distributed Redis token cache with hybrid local/Redis fallback, and COID-scoped cache keys enforcing tenant isolation at the caching layer.
- Owned end-to-end delivery of the **Logility Atlas Catalog Discovery Agent** — a Langflow + Azure OpenAI conversational agent for natural-language MCP tool discovery; authored the spec, built the MCP server, configured the agent, and wired full gateway routing.
- **Remediated 6+ CVEs** by integrating Bandit (SAST) + pip-audit (SCA) as a CI/CD pre-build gate that blocks Docker image creation on any high/medium-severity finding.
- Enforced **90%+ test coverage** and Ruff linting across 8 contributors as mandatory PR reviewer; owned the full release pipeline (sbox → dev → qa → stg → prod).

**Platform Entitlements** · Aug 2024 – Aug 2025 · `C#` `Vue 3` `ASP.NET Core` `Ory Keto` `Kafka` `PostgreSQL` `MongoDB` `AKS`

- **Tech Lead from day one** for a universal authorization service built on Google Zanzibar / Ory Keto (ReBAC); led backend, Vue 3 SPA, Kubernetes infra, and CI/CD across a **team of 6 engineers**.
- Cut redundant writes to the Keto authorization store at scale by designing **MetadataWorkerService** with delta-processing logic (toBeAdded / toBeDeleted diffs).
- Built the Groups management UI, Group Edit screen (with unsaved-changes protection), and User Details screen from scratch in Vue 3 / TypeScript.
- Delivered the team's **first structured production log visibility** — stood up Grafana + Loki dashboards from scratch, which became the observability baseline for later services.

**IdentityGateway — Aptean IAM Integration** · Mar 2024 – Apr 2026 · `C#` `ASP.NET Core` `IdentityServer4` `EF Core` `SQL Server` `AKS`

- **Lead engineer** for post-acquisition auth integration — built the Token Translation endpoint from scratch, exchanging Aptean IAM tokens for IDG tokens with **automatic user provisioning on first login** (no manual migration scripts).
- Extended the user model with Aptean COID/UOID claims; built tenant provisioning automation with schema validation and a warning system that surfaces misconfigured COID relationships before they reach production.
- Authored and implemented **3 Polaris specs**: .NET 10 migration, AutoMapper → Mapperly (compile-time zero-reflection mapping), and a ClaimTypes endpoint fix.
- Fixed critical auth bugs: duplicate-username during token translation, user deletion missing sub claim, and IAM configuration gaps that silently bypassed validation.

**Infrastructure.Cloud.Params** · Aug 2024 – May 2026 · `Azure Bicep` `Helm` `Azure Pipelines` `PowerShell`

- Owned the MCP Gateway Helm configuration rollout across all five environments (sbox → dev → qa → stg → prod) for the service launch.
- Designed the **tenant services registry** — a platform-wide single source of truth for tenant backend URLs, consumed at runtime by both Client Catalog and the MCP Gateway, replacing ad-hoc URL hardcoding.

#### Software Developer — R&D Platform Engineering (Logility Solutions) · Sep 2020 – Feb 2024

**Platform Airflow / PAM** · Sep 2021 – Aug 2023 · `Python` `Apache Airflow` `Docker` `Azure Pipelines` `Azure Bicep`

- **Primary owner (162 of ~205 commits — 79%)** of Logility's Apache Airflow deployment; drove three consecutive version upgrades (2.2.4 → 2.3.3 → 2.4.3 → 2.6.1).
- Integrated IDG OAuth2/OIDC SSO; built Azure Pipelines CI/CD and Azure Bicep IaC from scratch; added an Azure Service Bus provider for platform event publishing.
- Wrote DAGs for data processing, alerting, and scheduled jobs across the platform.

**AdapLink / LOG-RD-AL** · Oct 2020 – Jan 2024 · `Java 17` `Quarkus` `C# .NET 8` `MSSQL` `RabbitMQ` `Redis` `HashiCorp Consul`

- **Key contributor (355 commits)** to Logility's enterprise Java integration middleware; built LOM batch reporting infrastructure, CommonAdd integration with Redis AtomicLong sequential numbering, and the Hotfix Generator for automated customer patching.
- Extended HashiCorp Consul service discovery for dynamic endpoint resolution; built the UserManager CLI (Java) and AdapLinkEncryption utility (C# .NET 8) to fill developer-tooling gaps.
- **Led Log4Shell (CVE-2021-44228) remediation** — patched Log4j2 across **160+ modules** through 5 version upgrades; managed 8 platform releases (21.02.1 – 24.01.1).

**AdapLink Templates** · Sep 2020 – Aug 2023 · `Python` `XML` `PowerShell` `Azure Pipelines`

- **2nd highest contributor** building configuration-as-code ERP integration templates for supply chain customers (SAP, Oracle, JDE).
- Built the IBP-ATP/CTP integration template with batch-wise processing for high-volume order flows; created MPO and VOYAGER IO Cloud Sync templates; extended SAP/HANA templates with ObjectStore and VBFA support.
- Created Azure Pipelines CI/CD from scratch with versioned artifact generation; introduced pytest and wrote the project's **first automated test suite**.

**Identity.ProviderConfiguration** · Nov 2023 – Jan 2024 · `C#` `Vue 3` `ASP.NET Core` `Redis` `Docker` `AKS`

- Implemented read-only UI mode for OIDC/SAML provider forms end-to-end: Vue 3 components, validation refactor, xUnit + Vitest tests, Azure Pipelines CI, and Bicep IaC.

#### Integration Engineer — ERP Data Integration (AdapChain Solutions) · Mar 2014 – Sep 2020

- Owned complete integration projects end-to-end for enterprise customers including **SEI (7-Eleven), ATK, and VISTA** — handled direct customer communication, solution design, and delivery solo; integrated SAP HANA, Oracle EBS, and Microsoft NAV alongside daily delta file feeds into Logility's supply chain planning platform.
- Built rules-based transformation programs and supply/demand data models for Logility Voyager covering demand planning, supply planning, replenishment, production planning, and inventory optimization.
- Designed standard integration templates for SAP, Oracle, and JDE ERP systems deployed across multiple customer engagements.
- Served as **Release Master** — coordinating regression tests, documentation, and versioned releases; handled Change Control board responsibilities and post-implementation customer support.

## Personal Projects

**mcpbin** *(Deployed · Python · FastMCP · HuggingFace Spaces)* — A diagnostic MCP server with predictable, documented responses for every protocol feature, for testing MCP clients without throwaway servers. huggingface.co/spaces/ruhullasheik/mcpbin

## Education

**M.Tech** — JNTU Kakinada, 2013 | 91% · **B.Tech** — JNTU Kakinada, 2011 | 71%

## Certifications

Apache Airflow Fundamentals — Astronomer (Credly)
