import pandas as pd
import bar_chart_race as bcr
from pandas.core.frame import DataFrame

def grafico_dinamico(
        df: DataFrame, 
        titulo_sumarizacao: str, 
        titulo_grafico: str,
        filename: str = None) -> None:
    """
    Cria um gráfico dinâmico de barra utilizando a biblioteca bar_chart_race.

    Args:
        df (DataFrame): DataFrame contendo os dados a serem visualizados no gráfico.
        titulo_sumarizacao (str): Título para a sumarização dos valores nas barras.
        titulo_grafico (str): Título do gráfico.
        filename (str, optional): Nome do arquivo de saída do gráfico (.mp4). Se None, o gráfico será exibido em uma janela. 
                                  Defaults to None.
    """
    try:
        return bcr.bar_chart_race(
            df=df,
            filename=filename,
            orientation='h',
            sort='desc',
            n_bars=6,
            fixed_order=False,
            fixed_max=True,
            steps_per_period=10,
            interpolate_period=False,
            label_bars=True,
            bar_size=.95,
            period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
            period_fmt='%B %d, %Y',
            period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                            's': f'{titulo_sumarizacao}: {v.nlargest(6).sum():,.0f}',
                                            'ha': 'right', 'size': 8, 'family': 'Courier New'},
            perpendicular_bar_func='median',
            period_length=500,
            figsize=(5, 3),
            dpi=144,
            cmap='dark12',
            title=f'{titulo_grafico}',
            title_size='',
            bar_label_size=7,
            tick_label_size=7,
            # shared_fontdict={'family' : 'Helvetica', 'color' : '.1'},
            scale='linear',
            writer=None,
            fig=None,
            bar_kwargs={'alpha': .7},
            filter_column_colors=False
        )
    except Exception as e:
        print(f"Erro ao gerar o gráfico: {e}")