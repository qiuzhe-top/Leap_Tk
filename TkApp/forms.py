from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# class CommentForm(forms.Form):
#     con_tyoe = forms.Charfield()
class Subject_form(forms.Form):
    subject_form=forms.CharField(widget=CKEditorUploadingWidget())