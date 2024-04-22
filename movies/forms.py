from django.forms import ModelForm

from .models import Movie

class MovieForm(ModelForm):

  """
  Formulario de creación de películas
  """

  class Meta:
      model = Movie
      fields = ('title', )
