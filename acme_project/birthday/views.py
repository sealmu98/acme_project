from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django.urls import reverse_lazy

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


# Наследуем класс от встроенного ListView:
class BirthdayListView(ListView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    # ...и даже настройки пагинации:
    paginate_by = 10


class BirthdayCreateView(CreateView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # Этот класс сам может создать форму на основе модели!
    # Нет необходимости отдельно создавать форму через ModelForm.
    # Указываем имя формы:
    form_class = BirthdayForm


class BirthdayUpdateView(UpdateView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # Указываем имя формы:
    form_class = BirthdayForm


class BirthdayDeleteView(DeleteView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # Указываем namespace:name страницы, куда будет перенаправлен пользователь
    # после создания объекта:
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(DetailView):
    # Указываем модель, с которой работает CBV...
    model = Birthday

    def get_context_data(self, **kwargs):
        # Получаем словарь контекста:
        context = super().get_context_data(**kwargs)
        # Добавляем в словарь новый ключ:
        context['birthday_countdown'] = calculate_birthday_countdown(
            # Дату рождения берём из объекта в словаре context:
            self.object.birthday
        )
        # Возвращаем словарь контекста.
        return context
