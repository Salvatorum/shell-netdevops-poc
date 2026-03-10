# Shell Infrastructure PoC: NetDevOps Junior Lab

## 🎯 Objetivo
Demostrar la integración de redes tradicionales con prácticas modernas de DevOps, automatizando el despliegue de una API sobre un cluster de Kubernetes local y asegurando la conectividad entre nodos híbridos (Windows/Arch Linux).

## 🛠️ Stack Tecnológico
- **OS:** Arch Linux (Thinkpad T410) & Windows 10.
- **Orquestación:** Kubernetes (Kind) & Docker Compose.
- **Automatización:** Ansible (Configuración de Firewall y Dependencias).
- **Lenguajes:** Python (Monitoreo de Capa 7) & Bash.
- **Redes:** Modelo OSI, Protocolos TCP/IP, DNS Local, ICMP.

## 🌐 Arquitectura de Red
- **Segmento LAN:**  {{ network_address }}
- **Servidor (Arch):** {{ server_ip }} (IP Estática)
- **Cliente (Windows):** {{ client_ip }}
- **Resolución DNS:** `api.shell-local.com` apuntando al nodo de Kubernetes.

## 🚀 Cómo ejecutar este laboratorio
1. **Provisionamiento:** Ejecutar `ansible-playbook -i ansible/inventory.ini ansible/setup_node.yml`.
2. **Despliegue K8s:** Ejecutar `kubectl apply -f kubernetes/shell-api.yaml`.
3. **Monitoreo:** Correr `python monitoring/network_checker.py` para validar la disponibilidad del Ingress.
