import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
import argparse
import boto3
from sqlalchemy import create_engine

def save_model_to_s3(model, bucket_name, model_filename):
    s3 = boto3.client('s3')
    local_model_path = model_filename
    
    # Salvar o modelo localmente antes de enviá-lo para o S3

    joblib.dump(model, local_model_path)
    print(f"Modelo salvo localmente em {local_model_path}")

    # Enviar o modelo para o S3
    with open(local_model_path, 'rb') as f:
        s3.upload_fileobj(f, bucket_name, model_filename)
    print(f"Modelo salvo no S3 em s3://{bucket_name}/{model_filename}")

def main():
    print("Iniciando o script...")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--db-user', type=str, required=True, help="Usuário do banco de dados")
    parser.add_argument('--db-password', type=str, required=True, help="Senha do banco de dados")
    parser.add_argument('--db-host', type=str, default='database-1.cby6yae8mp75.us-east-1.rds.amazonaws.com', help="Host do banco de dados")
    parser.add_argument('--db-name', type=str, required=True, help="Nome do banco de dados")
    parser.add_argument('--output-model', type=str, default='model/model.joblib', help="Caminho para salvar o modelo")
    args = parser.parse_args()

    print("Conectando ao banco de dados...")
    db_connection_str = f'mysql+pymysql://{args.db_user}:{args.db_password}@{args.db_host}/{args.db_name}'
    db_connection = create_engine(db_connection_str)

    print("Carregando dados do arquivo CSV...")
    df = pd.read_csv('hotel_reservations_altered.csv')
    
    # Verificar as colunas do DataFrame
    print("Colunas disponíveis no DataFrame:", df.columns.tolist())
    
    print("Preparando os dados...")
    if 'label_avg_price_per_room' in df.columns:
        X = df.drop(['label_avg_price_per_room'], axis=1)
        y = df['label_avg_price_per_room']

        categorical_cols = X.select_dtypes(include=['object']).columns
        print(f"Colunas categóricas encontradas: {categorical_cols}")

        label_encoders = {}
        for col in categorical_cols:
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col].astype(str))
            label_encoders[col] = le

        if X.shape[1] > 1000:
            print("Reduzindo a dimensionalidade dos dados...")
            pca = PCA(n_components=100)
            X = pca.fit_transform(X)

        print(f"Tamanho do dataset: {X.shape}")

        print("Dividindo os dados...")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        print("Treinando o modelo...")
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        print("Avaliar o modelo...")
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f'Accuracy: {accuracy}')

        print("Salvando o modelo...")
        save_model_to_s3(model, 'ivoaragaobucket', args.output_model)
    else:
        
        print("Coluna 'label_avg_price_per_room' não encontrada no DataFrame.")



if __name__ == '__main__':
    main()