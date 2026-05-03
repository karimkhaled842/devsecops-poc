# StackRox (Red Hat Advanced Cluster Security) Comprehensive Guide

StackRox (now known as Red Hat Advanced Cluster Security or RHACS) is a Kubernetes-native security platform. It provides security and compliance across the entire build, deploy, and runtime lifecycle of your containerized applications.

## 🌟 Core Features

### 1. Vulnerability Management
StackRox continuously scans container images and cluster nodes for known vulnerabilities (CVEs).
- **Image Scanning:** Integrates with CI/CD to scan images before they are pushed to the registry or deployed.
- **Node Scanning:** Examines Kubernetes nodes for host-level vulnerabilities.
- **Prioritization:** Ranks vulnerabilities based on fixability and exploitability in your specific environment so you know what to patch first.

### 2. Risk Profiling
StackRox assigns a dynamically calculated "Risk Score" to every deployment in your cluster.
- **Context-Aware:** The score factors in vulnerabilities, RBAC permissions (e.g., cluster-admin access), network reachability, and runtime behavior.
- **Actionable:** Helps security teams immediately identify and prioritize which deployments need urgent attention.

### 3. Network Graph & Microsegmentation
A visual representation of all network traffic within your cluster.
- **Visibility:** Shows active and allowed network connections between namespaces and deployments.
- **Policy Generation:** Can automatically generate Kubernetes Network Policies based on observed baseline traffic to enforce "least privilege" networking.
- **Simulation:** Allows you to simulate network policies before applying them to avoid breaking application connectivity.

### 4. Configuration Management & Compliance
Monitors cluster, node, and deployment configurations against industry standards.
- **Standards Supported:** CIS Kubernetes Benchmarks, HIPAA, PCI-DSS, NIST, SOC 2.
- **Continuous Checks:** Identifies misconfigurations (e.g., missing resource limits, containers running as root, exposed secrets, privileged pods).

### 5. Runtime Threat Detection
Monitors active workloads for suspicious or malicious behavior using eBPF at the kernel level.
- **Process Execution:** Detects anomalous process executions (e.g., `nmap`, crypto-miners, package managers running in production).
- **Interactive Shells:** Alerts or blocks when someone `exec`s into a running pod.
- **Network Anomalies:** Identifies unexpected external connections or lateral movement attempts.

### 6. Policy Management & Enforcement
A powerful policy engine with hundreds of out-of-the-box and customizable rules.
- **Lifecycle Phases:** Policies can be enforced at the **Build** (CI/CD), **Deploy** (Admission Controller), or **Runtime** phases.
- **Enforcement Actions:** Can fail a CI pipeline, block a deployment from being created, or automatically kill a running pod if it violates critical security policies.

---

## 🧭 How to Navigate the StackRox UI

When you log into the StackRox Central UI, you'll use the left-hand navigation menu to access different features. Here is how to navigate the main sections:

### 📊 Dashboard
- **What it is:** The default landing page.
- **How to use it:** Use this for a high-level overview of your cluster's security posture. It shows policy violations over time, top risky deployments, and aging vulnerabilities at a glance.

### ⚠️ Violations
- **What it is:** A chronological log of every policy that has been triggered.
- **How to use it:** Review alerts, see which deployment caused the violation, and understand what phase (Build, Deploy, Runtime) it occurred in. You can also review remediation steps and mark violations as resolved here.

### 🎯 Risk
- **What it is:** A prioritized list of your deployments ordered by their dynamically calculated Risk Score.
- **How to use it:** Start your daily security remediation here. Click on the most risky deployment to see *why* it's risky (e.g., it has critical CVEs, is running as root, and is exposed to the internet).

### 🕸️ Network Graph
- **What it is:** An interactive map of your cluster's network.
- **How to use it:** Select a namespace to visualize traffic. Use the "Active" toggle to see actual traffic vs. "Allowed" to see what your Network Policies permit. Use the "Network Policy Simulator" to generate, test, and download new YAML manifests for network isolation.

### 🛡️ Vulnerability Management
- **What it is:** Deep dive into CVEs across images, deployments, and nodes.
- **How to use it:** Generate reports for compliance and auditing. Find specific CVEs (like Log4Shell) and instantly see which deployments are affected and whether a fix/patch is available in a newer image tag.

### 📋 Compliance
- **What it is:** The hub for industry standards and audits.
- **How to use it:** Select a standard (like the CIS Kubernetes Benchmark) to see your pass/fail rate across clusters and namespaces. Export detailed CSV/PDF reports for auditors.

### ⚙️ Platform Configuration (Administration)
*Found at the bottom of the navigation menu.*
- **Integrations:** Connect StackRox to your CI/CD pipelines, image registries (Docker Hub, AWS ECR, Quay), and notification tools (Slack, Jira, Email, PagerDuty).
- **Access Control:** Manage users, roles, and SSO integration (SAML, OIDC).
- **Clusters:** Manage the Kubernetes clusters that StackRox is monitoring (adding new secured clusters or removing old ones).
- **System Policies:** Create, edit, and enable/disable the security policies that drive alerts and enforcement.
