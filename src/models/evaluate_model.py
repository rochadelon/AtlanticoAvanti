# -*- coding: utf-8 -*-
import logging
import pickle
import os
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, precision_recall_curve, auc, average_precision_score
import matplotlib.pyplot as plt
import seaborn as sns


def evaluate_model(model_path, test_data_path, output_dir):
    """
    Avalia o desempenho do modelo nos dados de teste.
    
    Parameters:
    ----------
    model_path : str
        Caminho para o modelo treinado
    test_data_path : str
        Caminho para os dados de teste
    output_dir : str
        Diretório para salvar os resultados
    """
    logger = logging.getLogger(__name__)
    logger.info('Iniciando avaliação do modelo')
    
    # Criar diretório de saída se não existir
    os.makedirs(output_dir, exist_ok=True)
    
    # Carregar modelo
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    # Carregar dados de teste
    df_test = pd.read_csv(test_data_path)
    X_test = df_test.drop('target', axis=1)
    y_test = df_test['target']
    
    # Fazer predições
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    
    # Calcular métricas
    report = classification_report(y_test, y_pred, output_dict=True)
    df_report = pd.DataFrame(report).transpose()
    df_report.to_csv(f"{output_dir}/classification_report.csv")
    logger.info('Relatório de classificação salvo')
    
    # Matriz de confusão
    plt.figure(figsize=(10, 8))
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Matriz de Confusão')
    plt.ylabel('Valor Real')
    plt.xlabel('Valor Predito')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/confusion_matrix.png")
    plt.close()
    logger.info('Matriz de confusão salva')

    # Curva ROC
    fpr, tpr, thresholds = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)
    
    plt.figure(figsize=(10, 8))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'Curva ROC (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Taxa de Falsos Positivos')
    plt.ylabel('Taxa de Verdadeiros Positivos')
    plt.title('Receiver Operating Characteristic (ROC)')
    plt.legend(loc="lower right")
    plt.savefig(f"{output_dir}/roc_curve.png")
    plt.close()
    logger.info('Curva ROC salva')
    
    # Curva Precision-Recall
    precision, recall, _ = precision_recall_curve(y_test, y_proba)
    avg_precision = average_precision_score(y_test, y_proba)
    
    plt.figure(figsize=(10, 8))
    plt.plot(recall, precision, color='green', lw=2, label=f'Precision-Recall (AP = {avg_precision:.2f})')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Curva Precision-Recall')
    plt.legend(loc="lower left")
    plt.savefig(f"{output_dir}/precision_recall_curve.png")
    plt.close()
    logger.info('Curva Precision-Recall salva')
    
    # Salvar métricas em um arquivo JSON
    metrics = {
        'accuracy': report['accuracy'],
        'precision': report['weighted avg']['precision'],
        'recall': report['weighted avg']['recall'],
        'f1_score': report['weighted avg']['f1-score'],
        'roc_auc': roc_auc,
        'avg_precision': avg_precision
    }
    
    pd.Series(metrics).to_json(f"{output_dir}/metrics.json")
    logger.info('Métricas principais salvas em formato JSON')
    
    logger.info('Avaliação concluída')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    evaluate_model('models/model.pkl', 
                  'data/processed/test_dataset.csv',
                  'reports')
