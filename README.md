# Shell Infrastructure PoC: NetDevOps Junior Lab

![Arch Linux](https://img.shields.io/badge/OS-Arch_Linux-1793D1?style=flat-square&logo=arch-linux&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Orchestration-Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Ansible](https://img.shields.io/badge/Automation-Ansible-EE0000?style=flat-square&logo=ansible&logoColor=white)
![Python](https://img.shields.io/badge/Scripting-Python-3776AB?style=flat-square&logo=python&logoColor=white)

## Descripción General
Este repositorio documenta una Prueba de Concepto (PoC) enfocada en la integración de redes tradicionales con prácticas modernas de DevOps. El proyecto automatiza el despliegue de una API sobre un clúster local de Kubernetes, garantizando la conectividad, el enrutamiento y la seguridad entre nodos híbridos en una red local.

## Arquitectura y Topología de Red

La infraestructura simula un entorno cliente-servidor tradicional que interactúa con un entorno de orquestación de contenedores moderno.

```mermaid
graph TD
    subgraph "LAN Segment: 192.168.0.0/24"
        Client[Cliente Windows 10<br/>IP: 192.168.0.23] -->|Resolución DNS / HTTP| Server
        
        subgraph Server [Servidor Arch Linux / Thinkpad T410 <br/>IP Estática: 192.168.0.21]
            Ingress{K8s Ingress Controller}
            API[Shell API Pods]
            
            Ingress -->|Enrutamiento de Capa 7| API
        end
    end
    
    classDef client fill:#2b5797,stroke:#1e3e6b,stroke-width:2px,color:#fff;
    classDef server fill:#1793d1,stroke:#106a96,stroke-width:2px,color:#fff;
    class Client client;
    class Server server;
