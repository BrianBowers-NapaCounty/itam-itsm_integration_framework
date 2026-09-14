# Security Considerations for Capybara Integration

<img class="capybara-right" width="250px" src="/en/latest/_images/AF.png" alt="Capybara security guard examining binary data" style="filter: sepia(25%);  shape-outside: ellipse(100% 100% at 50% 50%) !important;">Integrating IT asset management and service management systems with ArcGIS Indoors through the Capybara Framework creates powerful operational capabilities, but it also introduces important security responsibilities. By design, Capybara connects systems that manage assets, facilities, and workflows, often exposing spatial context that can be sensitive if mishandled. Security must therefore be considered from the outset of the integration, not added later as an afterthought. The following guidance highlights key areas to consider and provides practical advice for implementing Capybara in a secure, well-governed manner.

## Key Security Points for Capybara Integration

* **[Authentication & Authorization](#authentication--authorization)**: Use modern protocols like SAML or OAuth 2.0 to sync user identities between ArcGIS and ServiceNow. Ensure that service accounts used for integration have the minimum necessary permissions (principle of least privilege).
* **[Data Security in Transit](#data-security-in-transit)**: Enforce HTTPS/TLS for all communication between ArcGIS (Enterprise or Online) and ServiceNow to prevent man-in-the-middle attacks.
* **[Data Security at Rest](#data-security-at-rest)**: Sensitive facility or asset data stored in either system should be encrypted. If using custom data feeds, ensure the database storing the shared information is secure.
* **[API Security & Access Control](#api-security--access-control)**: Restrict API access to specific IP addresses (IP-based access controls). Disable public access to ArcGIS Server Manager or Portal Admin directories.
* **[Data Minimization](#data-minimization)**: Only sync necessary data. For instance, avoid transferring detailed, sensitive, or high-security, restricted-access, or private interior space details unless absolutely required for the service ticket.
* **[Controlled Data Exposure](#controlled-data-exposure)**: Use view-based feature layers for sharing, ensuring that mobile users or facility managers only see the floor plans and assets relevant to their specific role, rather than full, raw GIS datasets.
* **[Audit Logging](#audit-logging)**: Implement thorough logging for API requests between ArcGIS and ServiceNow to track who accessed or modified asset data, ensuring accountability. 

---

## Authentication & Authorization

Strong authentication and authorization form the foundation of a secure Capybara integration. Wherever possible, ArcGIS (Enterprise or ArcGIS Online) and ITSM platforms such as ServiceNow should rely on centralized identity management using modern protocols like SAML or OAuth 2.0. This allows user identities and roles to be managed consistently across systems, reducing the risk of orphaned accounts or inconsistent access levels.

Service accounts used for system-to-system integration deserve special attention. These accounts should be dedicated, non-interactive accounts with clearly defined purposes and strictly limited permissions. Applying the principle of least privilege ensures that if an account is compromised, the potential impact is minimized. Periodic review of roles and permissions helps confirm that access still aligns with current operational needs.

## Data Security in Transit

Capybara integrations depend on frequent data exchange between systems, making protection of data in transit essential. All communication between ArcGIS components and ITSM platforms should be enforced over HTTPS with strong TLS configurations. This protects against interception, tampering, and man-in-the-middle attacks.

In addition to encryption, teams should consider network-level protections such as firewalls and secure routing between systems. When integrations span on-premises and cloud environments, attention should be paid to trusted network paths and secure gateways. Treat every integration endpoint as a potential attack surface and secure it accordingly.

## Data Security at Rest

Data at rest includes asset records, spatial layers, floor plans, and any intermediate or cached datasets used by Capybara. Sensitive facility or asset data should be encrypted using mechanisms supported by the underlying platforms, whether that data resides in ArcGIS datastores, ITSM databases, or custom integration components.

If custom data feeds, staging tables, or middleware databases are used, they must be secured to the same standard as the primary systems. This includes strong access controls, patching, backup protection, and alignment with organizational security policies. Securing data at rest helps ensure that even if storage systems are accessed improperly, the information remains protected.

## API Security & Access Control

APIs are the connective tissue of a Capybara implementation, and they must be tightly controlled. Access to ArcGIS and ITSM APIs should be restricted to known, trusted sources using techniques such as IP-based access controls or private network endpoints. Public exposure of administrative endpoints should be avoided.

Administrative interfaces like ArcGIS Server Manager or Portal Admin directories should be disabled or restricted from public access whenever possible. API tokens and credentials should be rotated regularly and stored securely. By limiting who and what can call APIs, teams reduce the likelihood of misuse or unauthorized automation.

## Data Minimization

Not all data needs to be shared to achieve Capybara’s goals. A deliberate data minimization strategy reduces both security risk and complexity. Teams should carefully evaluate which attributes, asset types, and spatial details are truly required to support service workflows and analytics.

For example, detailed interior space classifications or high-security areas may not be necessary for resolving a typical service ticket. Avoid syncing sensitive or restricted details unless there is a clear, documented business requirement. Sharing less data means there is less data to protect and less risk if something goes wrong.

## Controlled Data Exposure

Even when data is shared, it should not be exposed uniformly to all users. Capybara implementations benefit from using view-based feature layers, filtered datasets, and role-based sharing models. This ensures that users see only the floor plans, assets, and attributes relevant to their role and responsibilities.

Mobile users, contractors, or facility staff may require a limited, task-focused view rather than access to full GIS datasets. Controlled exposure supports operational efficiency while reducing the chance of accidental disclosure or misuse of sensitive information.

## Audit Logging

Audit logging provides visibility and accountability across the integration. Both ArcGIS and ITSM platforms should be configured to log API requests, data changes, and access events related to Capybara workflows. Logs should capture who accessed or modified data, when the action occurred, and what was affected.

Automations and scripts can be used to analyze logs, flag anomalous activity, and generate regular reports. Effective audit logging not only supports security monitoring, but also helps with troubleshooting, compliance, and continuous improvement of the integration over time.

---

Taken together, these practices help ensure that a Capybara integration is not only powerful and functional, but also secure, trustworthy, and aligned with organizational governance expectations.
