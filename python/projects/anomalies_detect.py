import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("AAPL_stock_data.csv")

def info_column():
    return print("Colonnes disponibles :", df.columns.tolist())

def detect_normal_distribution(column, track):
    for i in range(0, len(df), track):
        # .iloc[i:i+track] => sélectionne les lignes de i jusqu’à (i+track) EXCLUS
        # .dropna() => enlève les valeurs manquantes (NaN)
        bloc = df[column].iloc[i:i+track].dropna()

        if len(bloc) >= 3:
            # Moyenne du bloc (mean) et écart-type (standard deviation)
            mean = bloc.mean()
            std = bloc.std()

            # np.linspace(a, b, 100) => crée un tableau de 100 valeurs entre a et b
            # Ici on génère 100 points entre (mean - 4*std) et (mean + 4*std)
            x = np.linspace(mean - 4*std, mean + 4*std, 100)

            # Formule de la courbe normale (fonction de densité de probabilité)
            # C’est l’équation mathématique d’une "gaussienne"
            # (1 / (σ * √(2π))) * e^(-0.5 * ((x - μ) / σ)^2)
            normal_pdf = (1/(std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean)/std)**2)

            # Crée une nouvelle figure de taille 8x4 pouces
            plt.figure(figsize=(8, 4))

            # bins=15 → 15 barres ; density=True → normalisé (aire = 1) ; alpha=0.6 → transparence
            plt.hist(bloc, bins=15, density=True, alpha=0.6, label='Données du bloc')

            # linewidth=2 → épaisseur de la ligne
            plt.plot(x, normal_pdf, label='Courbe normale', linewidth=2)

            # f-string = permet d’intégrer des variables dans une chaîne
            # :.2f = formatage → 2 chiffres après la virgule (float → .2f)
            plt.title(f'Bloc {i//track + 1} | Moyenne = {mean:.2f}, Écart-type = {std:.2f}')

            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        else:
            print(f'Bloc {i//track + 1} | Trop petit')


detect_normal_distribution('Price', 30)
# info_column()