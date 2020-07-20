#导入表单,导入自带User,导入自己写得User_pro
from django import forms
from django.contrib.auth.models import User


#注册表单,
class RegForm(forms.Form):
    #表单详情
    name=forms.CharField(label="昵称",max_length=20,widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"请输入您的昵称"}))
    account=forms.CharField(label="账号",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"请输入账号,5-9位数字!"}))
    email=forms.CharField(label="邮箱",widget=forms.TextInput(attrs={"class":"form-control",'placeholder':"请输入邮箱"}))
    password=forms.CharField(label="密码",min_length=8,max_length=16,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"请输入8-20位字符密码!"}))
    password_again = forms.CharField(label="密码", min_length=8, max_length=16, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "请确认密码!"}))
    Birthday=forms.DateField(label="出生日期",required=False,widget=forms.DateInput(attrs={"class":"form-control","type":"date"}))
    Site=forms.CharField(label="住址",max_length=30,widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"请输入您的住址,可不填"}))
    Head_icon=forms.ImageField(label="头像",required=False,widget=forms.FileInput(attrs={"class":"form-control","placeholder":"选择jpg/jpeg格式图片!"}))

    #表单数据处理

    def clean_name(self):
        name=self.cleaned_data["name"]
        return name

    def clean_account(self):
        account=self.cleaned_data["account"]
        #如果账号已经存在,则返回错误信息,账号已近存在
        if account.isnumeric():
            if User.objects.filter(username=account).exits():
                raise forms.ValidationError("账号已被注册!")
            else:
                return account
        else:
            raise forms.ValidationError("账号含除数字外的字符")

    def clean_email(self):
        email=self.cleaned_data["email"]
        if User.objects.filter(email=email).exits():
            raise forms.ValidationError("该邮箱已经被注册!")
        else:
            return email

    def clean_password_again(self):
        password=self.cleaned_data["password"]
        password_again = self.cleaned_data["password_again"]
        if password !=password_again:
            raise forms.ValidationError("两次密码不一致,请重新输入")
        else:
            return password_again

    def clean_Birthday(self):
        birthday=self.cleaned_data["Birthday"]
        return birthday

    def clean_Site(self):
        site=self.cleaned_data["Site"]
        return site

    def clean_Head_icon(self):
        head_icon=self.cleaned_data["Head_icon"]
        return head_icon



class LoginForm(forms.Form):
    account = forms.CharField(label="账号", max_length=15,widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"请输入您的账号","οnfοcus":"this.placeholder=''"}))
    password=forms.CharField(label="密码",max_length=16,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"请输入您的密码"}))

    def clean_account(self):
        account=self.cleaned_data["account"]
        return account

    def clean_password(self):
        password=self.cleaned_data["password"]
        return password