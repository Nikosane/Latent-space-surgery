from models.base_gan import BaseGAN
from models.base_vae import BaseVAE

class DisentangledLatentModel:
    def __init__(self, model_type='gan', latent_dim=512):
        self.latent_dim = latent_dim
        if model_type == 'gan':
            self.model = BaseGAN(latent_dim)
        elif model_type == 'vae':
            self.model = BaseVAE(latent_dim)
        else:
            raise ValueError("Model type must be 'gan' or 'vae'")

    def train(self, data_loader):
        self.model.train(data_loader)

    def edit_latent(self, z, attribute, direction_vector):
        # Apply surgery by modifying specific attribute direction in latent space
        return z + direction_vector

    def interpolate(self, z1, z2, alpha=0.5):
        # Linear interpolation between two latent codes
        return (1 - alpha) * z1 + alpha * z2
