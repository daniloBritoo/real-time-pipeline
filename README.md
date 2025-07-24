# real-time-pipeline

Este projeto implementa um pipeline de processamento de dados em tempo real utilizando Apache Kafka, Spark Structured Streaming e Docker.

## Descrição

O sistema simula sensores de temperatura que enviam dados continuamente para um tópico Kafka. Um consumidor Spark lê esses dados em tempo real, processa e salva os resultados em arquivos CSV.

## Estrutura do Projeto

- `producer/producer.py`: Produtor Kafka que gera dados simulados de sensores e envia para o tópico `temperature_sensor`.
- `consumer/consumer.py`: Consumidor Spark que lê dados do Kafka, processa e salva em CSV.
- `docker-compose.yaml`: Orquestra os serviços Kafka e Zookeeper via Docker.

## Como Executar

1. **Suba os serviços Kafka e Zookeeper:**
   ```bash
   docker-compose up -d
   ```
2. **Execute o produtor:**
   ```bash
   python producer/producer.py
   ```
3. **Execute o consumidor:**
   ```bash
   python consumer/consumer.py
   ```

Os arquivos processados serão salvos em `streaming_insert/`.

## Requisitos
- Docker
- Python 3.8+
- Apache Spark
- Bibliotecas: kafka-python, pyspark

## Observações
- O pipeline é totalmente configurável e pode ser adaptado para outros tipos de dados.
- O projeto é ideal para estudos de streaming, integração de dados e Big Data.

