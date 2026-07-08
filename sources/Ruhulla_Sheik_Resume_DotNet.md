# Ruhulla Sheik

**Senior Software Engineer · .NET / Azure Solutions Architect · Tech Lead**

sk.ruhulla@gmail.com | +91 9035786999 | linkedin.com/in/ruhullasheik | github.com/ruhullasheik | Bangalore, India

## Professional Summary

.NET and Azure platform engineer operating at architect level, with **12+ years at a single enterprise SaaS company through three acquisitions**. Core member of the team that migrated supply-chain tooling from a **monolith into multi-tenant cloud-native microservices on Azure (AKS)** — API gateway, event-driven messaging, and CI/CD. Expert in **C# / .NET Core and ASP.NET Core** built on SOLID, Clean Architecture, and secured OpenAPI REST services. **Tech Lead and sole mandatory PR reviewer for 8 engineers**, owning architectural governance, mentoring, and incident resolution. Also a daily practitioner of **AI-augmented engineering with Claude Code** — spec-driven development, AI guardrails, and secure code generation — having shipped a production MCP AI gateway and a Langflow + Azure OpenAI agent.

## Technical Skills

**Languages:** C#, Python, Java, TypeScript, SQL, PowerShell<br>
**Cloud & Architecture:** Azure (AKS, Bicep, Pipelines, Service Bus, Key Vault, App Insights, Redis Cache, Load Test, Logic Apps, ADF), Microservices, API Gateway, Event-Driven Architecture, Monolith-to-Microservices Migration<br>
**Patterns & Practices:** SOLID, Clean Architecture, Design Patterns, REST / OpenAPI / Swagger, Domain-Driven design<br>
**.NET Stack:** .NET Core / .NET 8–10, ASP.NET Core, Entity Framework Core, IdentityServer4, AutoMapper / Mapperly, xUnit<br>
**AI-Augmented Engineering:** Claude Code, Spec-Driven Development, Model Context Protocol (MCP), FastMCP, Langflow, Azure OpenAI, AI guardrails<br>
**Containers & DevOps:** Docker, Kubernetes, Helm, Azure Pipelines (CI/CD), Infrastructure-as-Code (Azure Bicep)<br>
**Databases:** SQL Server / Azure SQL, PostgreSQL, MongoDB / Cosmos DB<br>
**Security:** OAuth2, OpenID Connect (OIDC), JWT / JWKS, SAML 2.0, Ory Keto (ReBAC), OWASP, Bandit (SAST), pip-audit (SCA)<br>
**Observability:** OpenTelemetry, Grafana, Loki, Azure Application Insights<br>
**Messaging:** Apache Kafka, Azure Service Bus, RabbitMQ

## Professional Experience

### Logility Solutions, an Aptean Company *(formerly AdapChain Solutions)* — Bangalore, India | Mar 2014 – Present

#### Senior Software Engineer / Tech Lead — Platform Engineering · Mar 2024 – Present

**Platform Entitlements** · Aug 2024 – Aug 2025 · `C#` `ASP.NET Core` `Vue 3` `Ory Keto` `Kafka` `PostgreSQL` `MongoDB` `AKS`

- **Tech Lead from day one** for a universal authorization service built on Google Zanzibar / Ory Keto (ReBAC); designed the architecture and led backend, Vue 3 SPA, Kubernetes infra, and CI/CD across a **team of 6 engineers**.
- Cut redundant writes to the Keto authorization store at scale by designing **MetadataWorkerService** with delta-processing logic (toBeAdded / toBeDeleted diffs) — an event-driven, idempotent pattern.
- Built the Groups management UI, Group Edit screen (with unsaved-changes protection), and User Details screen end-to-end in Vue 3 / TypeScript over secured ASP.NET Core APIs.
- Delivered the team's **first structured production log visibility** — stood up Grafana + Loki dashboards from scratch, the observability baseline for later services.

**IdentityGateway — Aptean IAM Integration** · Mar 2024 – Apr 2026 · `C#` `ASP.NET Core` `IdentityServer4` `EF Core` `SQL Server` `AKS`

- **Lead engineer** for post-acquisition auth integration — built the Token Translation endpoint from scratch, exchanging Aptean IAM tokens for IDG tokens (OAuth2/OIDC/JWT) with **automatic user provisioning on first login** (no manual migration scripts).
- Extended the user model with Aptean COID/UOID claims; built tenant provisioning automation with schema validation and a warning system that surfaces misconfigured relationships before they reach production.
- Authored and implemented **3 architecture specs**: .NET 10 migration, AutoMapper → Mapperly (compile-time zero-reflection mapping), and a ClaimTypes endpoint fix.
- Resolved critical auth incidents: duplicate-username during token translation, user deletion missing sub claim, and IAM configuration gaps that silently bypassed validation.

**MCP Gateway — AI-Augmented Platform** · Jan 2026 – May 2026 · `Python` `FastMCP` `FastAPI` `PostgreSQL` `Redis` `OpenTelemetry` `AKS`

- **Architected and shipped** a production AI gateway **serving 20,000+ API calls/day** across a multi-tenant Azure platform that auto-discovers OpenAPI specs and exposes them as tools — as **Tech Lead, lead contributor, and sole mandatory PR reviewer for 8 contributors**.
- Designed **instance-aware multi-tenant URL resolution** so one deployed gateway serves all tenants with isolated per-tenant routing, eliminating per-tenant deployments; built IAM token translation and a distributed Redis token cache with hybrid local/Redis fallback.
- Owned the **Logility Atlas Catalog Discovery Agent** (Langflow + Azure OpenAI) end-to-end for natural-language tool discovery — practicing **spec-driven development with Claude Code** and AI guardrails throughout.
- **Remediated 6+ CVEs** by integrating Bandit (SAST) + pip-audit (SCA) as a CI/CD pre-build gate; enforced 90%+ test coverage across 8 contributors.

**Infrastructure.Cloud.Params** · Aug 2024 – May 2026 · `Azure Bicep` `Helm` `Azure Pipelines` `PowerShell`

- Owned Helm configuration rollout across **all five environments** (sbox → dev → qa → stg → prod) for the MCP Gateway launch.
- Designed the **tenant services registry** — a platform-wide single source of truth for tenant backend URLs, consumed at runtime by multiple services, replacing ad-hoc URL hardcoding.

#### Software Developer — R&D Platform Engineering (Logility Solutions) · Sep 2020 – Feb 2024

**AdapLink / LOG-RD-AL** · Oct 2020 – Jan 2024 · `Java 17` `Quarkus` `C# .NET 8` `MSSQL` `RabbitMQ` `Redis` `HashiCorp Consul`

- **Key contributor (355 commits)** to Logility's enterprise integration middleware; built LOM batch reporting infrastructure, CommonAdd integration with Redis AtomicLong sequential numbering, and the Hotfix Generator for automated customer patching.
- Extended HashiCorp Consul service discovery for dynamic endpoint resolution; built the UserManager CLI (Java) and AdapLinkEncryption utility (C# .NET 8).
- **Led Log4Shell (CVE-2021-44228) remediation** — patched Log4j2 across **160+ modules** through 5 version upgrades; managed 8 platform releases (21.02.1 – 24.01.1).

**Platform Airflow / PAM** · Sep 2021 – Aug 2023 · `Python` `Apache Airflow` `Docker` `Azure Pipelines` `Azure Bicep`

- **Primary owner (162 of ~205 commits — 79%)** of Logility's Apache Airflow deployment; drove **three consecutive version upgrades** and integrated IDG OAuth2/OIDC SSO.
- Built Azure Pipelines CI/CD and Azure Bicep IaC from scratch; added an Azure Service Bus provider for platform event publishing.

**Identity.ProviderConfiguration** · Nov 2023 – Jan 2024 · `C#` `Vue 3` `ASP.NET Core` `Redis` `Docker` `AKS`

- Implemented read-only UI mode for OIDC/SAML provider forms end-to-end: Vue 3 components, validation refactor, xUnit + Vitest tests, Azure Pipelines CI, and Bicep IaC.

#### Integration Engineer — ERP Data Integration (AdapChain Solutions) · Mar 2014 – Sep 2020

- Owned complete integration projects end-to-end for enterprise customers including **SEI (7-Eleven), ATK, and VISTA** — direct customer communication, solution design, and solo delivery; integrated SAP HANA, Oracle EBS, and Microsoft NAV into Logility's supply-chain planning platform.
- Built rules-based transformation programs and supply/demand data models; designed standard SAP/Oracle/JDE integration templates deployed across multiple customers.
- Served as **Release Master** — coordinating regression tests, documentation, versioned releases, and Change Control board responsibilities.

## Personal Projects

**mcpbin** *(Deployed · Python · FastMCP · HuggingFace Spaces)* — A diagnostic MCP server with predictable, documented responses for every protocol feature, for testing MCP clients without throwaway servers. huggingface.co/spaces/ruhullasheik/mcpbin

## Education

**M.Tech** — JNTU Kakinada, 2013 | 91% · **B.Tech** — JNTU Kakinada, 2011 | 71%

## Certifications

Apache Airflow Fundamentals — Astronomer (Credly)
