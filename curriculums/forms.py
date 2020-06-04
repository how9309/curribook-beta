from django import forms


class SearchForm(forms.Form):
    title = forms.CharField(label="")


class CreatorApplicationForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=11)
    title = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(CreatorApplicationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = '이름'
        self.fields['email'].widget.attrs['placeholder'] = '이메일'
        self.fields['title'].widget.attrs['placeholder'] = '제목'
        self.fields['message'].widget.attrs['placeholder'] = '내용을 입력해주세요 (만들고 싶은 커리큘럼의 간단한 주제 혹은 아이디어정도로도 충분합니다)'
        self.fields['phone'].widget.attrs['placeholder'] = '전화번호'
