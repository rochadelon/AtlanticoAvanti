# Guia de Contribuição

## Como contribuir com este projeto

### Estrutura do Código

Por favor, siga a estrutura de código existente ao adicionar novos recursos ou funcionalidades:

- Coloque código relacionado a processamento de dados em `src/data/`
- Coloque código relacionado a engenharia de features em `src/features/`
- Coloque código relacionado a modelos em `src/models/`
- Coloque visualizações em `src/visualization/`

### Estilo de Código

- Siga a PEP 8 para código Python
- Use docstrings para documentar funções e classes
- Escreva testes unitários para novas funcionalidades

### Fluxo de Trabalho Git

1. Crie uma branch para sua feature: `git checkout -b feature/nome-da-feature`
2. Faça commits atômicos: `git commit -m 'Adiciona recurso X'`
3. Envie para o repositório: `git push origin feature/nome-da-feature`
4. Abra um Pull Request

### Ambiente de Desenvolvimento

Recomendamos usar um ambiente virtual para desenvolvimento:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

Obrigado por contribuir!
