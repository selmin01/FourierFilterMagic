
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error as mse
from skimage.color import rgb2gray
from skimage.exposure import equalize_hist
from skimage.filters import gaussian

def apply_fourier_mask(image, mask_coordinates, mask_value=0):
    image_fourier = np.fft.fftshift(np.fft.fft2(image))
    for (x_start, x_end, y_start, y_end) in mask_coordinates:
        image_fourier[x_start:x_end, y_start:y_end] = mask_value
    processed_image = np.fft.ifft2(np.fft.ifftshift(image_fourier))
    processed_image = np.abs(processed_image)
    return image_fourier, processed_image

def evaluate_image(original_image, processed_image):
    processed_image_norm = (processed_image - np.min(processed_image)) / (np.max(processed_image) - np.min(processed_image))
    ssim_value = ssim(original_image, processed_image_norm, data_range=processed_image_norm.max() - processed_image_norm.min())
    mse_value = mse(original_image, processed_image_norm)
    return ssim_value, mse_value

def plot_results(original_image, image_fourier, processed_image, title_prefix, save_path):
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    f_size = 12

    ax[0].imshow(original_image, cmap='gray')
    ax[0].set_title('Imagem Original', fontsize=f_size)
    ax[0].axis('off')

    ax[1].imshow(np.log(np.abs(image_fourier)), cmap='gray')
    ax[1].set_title(f'{title_prefix}\nMáscara de Fourier', fontsize=f_size)
    ax[1].axis('off')

    ax[2].imshow(processed_image, cmap='gray')
    ax[2].set_title(f'{title_prefix}\nImagem Recuperada', fontsize=f_size)
    ax[2].axis('off')

    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()

def main():
    # Defina o caminho para o arquivo de imagem
    file_path = '/Users/anselmoramos/Documents/Files/PIM/Tarefa_2/FourierFilterMagic/images/folhas1.jpg'  # Substitua pelo caminho correto para sua imagem
    if not os.path.exists(file_path):
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        return
    
    # Carrega a imagem
    original_image = imread(file_path)

    if len(original_image.shape) == 3:
        original_image = rgb2gray(original_image)

    original_image = original_image / 255.0
    vertical_mask_coords = [(-590, -560, 955, 970), (590, 620, 955, 970)]
    horizontal_mask_coords = [(600, 615, 0, 955), (600, 615, -955, None)]
    combined_mask_coords = [(600, 610, 0, 950), (600, 610, -950, None), 
                            (0, 600, 955, 965), (-590, None, 955, 965)]

    if not os.path.exists('results'):
        os.makedirs('results')

    ver_fourier, ver_processed = apply_fourier_mask(original_image, vertical_mask_coords)
    ver_ssim, ver_mse = evaluate_image(original_image, ver_processed)
    plot_results(original_image, ver_fourier, ver_processed, "Vertical", 'results/vertical_result.png')
    print(f"SSIM Vertical: {ver_ssim:.4f}, MSE Vertical: {ver_mse:.4f}")

    hor_fourier, hor_processed = apply_fourier_mask(original_image, horizontal_mask_coords)
    hor_ssim, hor_mse = evaluate_image(original_image, hor_processed)
    plot_results(original_image, hor_fourier, hor_processed, "Horizontal", 'results/horizontal_result.png')
    print(f"SSIM Horizontal: {hor_ssim:.4f}, MSE Horizontal: {hor_mse:.4f}")

    comb_fourier, comb_processed = apply_fourier_mask(original_image, combined_mask_coords)
    comb_ssim, comb_mse = evaluate_image(original_image, comb_processed)
    plot_results(original_image, comb_fourier, comb_processed, "Vertical e Horizontal", 'results/combined_result.png')
    print(f"SSIM Vertical e Horizontal: {comb_ssim:.4f}, MSE Vertical e Horizontal: {comb_mse:.4f}")

    # Aplica equalização de histograma e filtro Gaussiano na melhor imagem recuperada (combinada)
    enhanced_image = equalize_hist(comb_processed)
    enhanced_image = gaussian(enhanced_image, sigma=1)
    enhanced_ssim, enhanced_mse = evaluate_image(original_image, enhanced_image)

    # Plota o melhor resultado comparado com a imagem original
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    f_size = 12

    ax[0].imshow(original_image, cmap='gray')
    ax[0].set_title('Imagem Original', fontsize=f_size)
    ax[0].axis('off')

    ax[1].imshow(enhanced_image, cmap='gray')
    ax[1].set_title('Melhor Resultado (Equalizado + Suavizado)', fontsize=f_size)
    ax[1].axis('off')

    plt.tight_layout()
    plt.savefig('/Users/anselmoramos/Documents/Files/PIM/Tarefa_2/FourierFilterMagic/results/best_result.png')
    plt.show()

    print(f"SSIM Melhorado: {enhanced_ssim:.4f}, MSE Melhorado: {enhanced_mse:.4f}")

if __name__ == "__main__":
    main()

