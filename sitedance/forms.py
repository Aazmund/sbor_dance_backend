from django import forms


class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=100, label='ФИО *', widget=forms.TextInput(attrs={'id': 'fio', 'name': 'fio'}))
    number = forms.CharField(max_length=100, label='Номер телефона *')
    # number = forms.CharField(max_length=100, label='Номер телефона', required='', id='number', type='tel')
    mail = forms.CharField(max_length=100, label='E-mail *')
    date = forms.CharField(max_length=100, label='Дата рождения *')
    parent_name = forms.CharField(max_length=100, label='Имя родителя/представителя *')
    vk_link = forms.CharField(max_length=100, label='ссылка на ВКонтакте', required='')
    comment = forms.CharField(widget=forms.Textarea, required='', label='Комментарий ')

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['name'].widget.attrs.update({'id': 'fio'})
        self.fields['number'].widget.attrs.update({'id': 'number'})
        self.fields['mail'].widget.attrs.update({'id': 'mail'})
        self.fields['date'].widget.attrs.update({'id': 'date'})
        self.fields['parent_name'].widget.attrs.update({'id': 'parent'})
        self.fields['vk_link'].widget.attrs.update({'id': 'vk'})
        # self.fields['comment'].widget.attrs.update({'type': 'textarea', 'id': 'com', 'cols': '30', 'rows': '7'})
