# from tutors.match.apps import PredictConfig
import pickle
from os import strerror

import sklearn
# from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CreateUserForm
from .models import *


# Create your views here.
def index(request):
    context = {}
    return render(request, 'match/index.html', context)


def login(request):
    context = {}
    return render(request, 'match/login.html', context)


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()  # create usercreation for

    context = {
        'form': form
    }
    return render(request, 'match/signup.html', context)


@login_required
def match(request):
    PassStudents = Pass.objects.all()
    FailStudents = Fail.objects.all()
    context = {
        'PassStudents': PassStudents,
        'FailStudents': FailStudents
    }
    return render(request, 'match/match.html', context)


@login_required
def adminpage(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'match/admin.html', context)


def pair(learn, tut):
    matchtable = Match.objects.all()
    matchtable = Match(student=learn, tutor=tut)
    matchtable.save()


def checkpair(learn):
    exist = Match.objects.filter(student=learn).exists()
    return exist


@login_required
def matchresult(request):
    AllTutors = Pass.objects.all()

    MathVTutors = Pass.objects.filter(learning_styles="Visual", area_of_interests="Mathematics")
    MathATutors = Pass.objects.filter(learning_styles="Auditory", area_of_interests="Mathematics")
    MathKTutors = Pass.objects.filter(learning_styles="Kinesthetic", area_of_interests="Mathematics")

    EngVTutors = Pass.objects.filter(learning_styles="Visual", area_of_interests="English")
    EngATutors = Pass.objects.filter(learning_styles="Auditory", area_of_interests="English")
    EngKTutors = Pass.objects.filter(learning_styles="Kinesthetic", area_of_interests="English")

    PhyVTutors = Pass.objects.filter(learning_styles="Visual", area_of_interests="Physics")
    PhyATutors = Pass.objects.filter(learning_styles="Auditory", area_of_interests="Physics")
    PhyKTutors = Pass.objects.filter(learning_styles="Kinesthetic", area_of_interests="Physics")

    AllLearners = Fail.objects.all()

    MathVLearners = Fail.objects.filter(learning_styles="Visual", area_of_interests="Mathematics")
    MathALearners = Fail.objects.filter(learning_styles="Auditory", area_of_interests="Mathematics")
    MathKLearners = Fail.objects.filter(learning_styles="Kinesthetic", area_of_interests="Mathematics")

    EngVLearners = Fail.objects.filter(learning_styles="Visual", area_of_interests="English")
    EngALearners = Fail.objects.filter(learning_styles="Auditory", area_of_interests="English")
    EngKLearners = Fail.objects.filter(learning_styles="Kinesthetic", area_of_interests="English")

    PhyVLearners = Fail.objects.filter(learning_styles="Visual", area_of_interests="Physics")
    PhyALearners = Fail.objects.filter(learning_styles="Auditory", area_of_interests="Physics")
    PhyKLearners = Fail.objects.filter(learning_styles="Kinesthetic", area_of_interests="Physics")

    for tutor in MathVTutors:
        for learner in MathVLearners:
            if checkpair(learner) == True:
                continue
            else:
                if tutor.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif learner.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif tutor.personality_styles == "Introvert":
                    if learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Introvert":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Feeling":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Intuitive":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                else:
                    print(str(tutor) + " can not be matched with " + str(learner))

    for tutor in MathATutors:
        for learner in MathALearners:
            if checkpair(learner) == True:
                continue
            else:
                if tutor.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif learner.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif tutor.personality_styles == "Introvert":
                    if learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Introvert":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Feeling":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Intuitive":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                else:
                    print(str(tutor) + " can not be matched with " + str(learner))

    for tutor in MathKTutors:
        for learner in MathKLearners:
            if checkpair(learner) == True:
                continue
            else:
                if tutor.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif learner.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif tutor.personality_styles == "Introvert":
                    if learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Introvert":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Feeling":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Intuitive":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                else:
                    print(str(tutor) + " can not be matched with " + str(learner))

    for tutor in EngVTutors:
        for learner in EngVLearners:
            if checkpair(learner) == True:
                continue
            else:
                if tutor.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif learner.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif tutor.personality_styles == "Introvert":
                    if learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Introvert":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Feeling":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Intuitive":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                else:
                    print(str(tutor) + " can not be matched with " + str(learner))

    for tutor in EngATutors:
        for learner in EngALearners:
            if checkpair(learner) == True:
                continue
            else:
                if tutor.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif learner.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif tutor.personality_styles == "Introvert":
                    if learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Introvert":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Feeling":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Intuitive":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                else:
                    print(str(tutor) + " can not be matched with " + str(learner))

    for tutor in EngKTutors:
        for learner in EngKLearners:
            if checkpair(learner) == True:
                continue
            else:
                if tutor.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif learner.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif tutor.personality_styles == "Introvert":
                    if learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Introvert":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Feeling":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Intuitive":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                else:
                    print(str(tutor) + " can not be matched with " + str(learner))

    for tutor in PhyVTutors:
        for learner in PhyVLearners:
            if checkpair(learner) == True:
                continue
            else:
                if tutor.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif learner.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif tutor.personality_styles == "Introvert":
                    if learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Introvert":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Feeling":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Intuitive":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                else:
                    print(str(tutor) + " can not be matched with " + str(learner))

    for tutor in PhyATutors:
        for learner in PhyALearners:
            if checkpair(learner) == True:
                continue
            else:
                if tutor.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif learner.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif tutor.personality_styles == "Introvert":
                    if learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Introvert":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Feeling":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Intuitive":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                else:
                    print(str(tutor) + " can not be matched with " + str(learner))

    for tutor in PhyKTutors:
        for learner in PhyKLearners:
            if checkpair(learner) == True:
                continue
            else:
                if tutor.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif learner.personality_styles == "Extrovert":
                    pair(learner, tutor)
                elif tutor.personality_styles == "Introvert":
                    if learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Introvert":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Feeling":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                elif tutor.personality_styles == "Intuitive":
                    if learner.personality_styles == "Extrovert":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Intuitive":
                        pair(learner, tutor)
                    elif learner.personality_styles == "Feeling":
                        pair(learner, tutor)
                else:
                    print(str(tutor) + " can not be matched with " + str(learner))

    matchings = Match.objects.all()
    print(matchings)

    context = {
        'matchings': matchings
    }
    return render(request, 'match/matchdisplay.html', context)


@login_required
def newprediction(request):
    context = {}

    # if request.method== 'POST':
    #     myform = InputForm(request.POST)
    #     if myform.is_valid():
    #         myform.save()
    #         return redirect('match')

    # else:
    #     myform = InputForm()
    # context = {
    #     'myform': myform
    # }
    return render(request, 'match/predict.html', context)


@login_required
def prediction(request):
    # if request.method== 'POST':
    #     myform = InputForm(request.POST)
    #     if myform.is_valid():
    #         # input_data = [[failures,Pstatus,guardian,higher,Walc,sex,G1,G2,G3]]
    #         # global G3
    #         # myform.instance.G3 = PredictConfig.loaded_model.predict(input_data)
    #         # G3 = myform.instance.G3
    #         # G3 = G3.astype(int)
    #         # G3 = G3 [0]

    #         myform.save()
    #         return redirect('match')

    # else:
    #     myform = InputForm()
    context = {
        # 'myform': myform
    }
    return render(request, 'match/prediction.html', context)


def do_classify(features):
    features = {k: int(v) for k, v in features.items()}
    model = pickle.load(open("C:/Users/Bube/Desktop/bolu/tutors/match/static/datasets/classification.sav", 'rb'))
    row = (list(features.values()))
    print(row)
    prediction = model.predict([row])[0]
    if prediction == 2:
        return 'Pass'
    elif prediction == 1:
        return 'Fail'


@login_required
def prediction2(request):
    context = {}
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    stid = request.POST.get('stid')

    sex = request.POST.get('sex')
    context['sex'] = sex

    age = request.POST.get('age')
    context['age'] = age

    Pstatus = request.POST.get('Pstatus')
    context['Pstatus'] = Pstatus

    guardian = request.POST.get('guardian')
    context['guardian'] = guardian

    higher = request.POST.get('higher')
    context['higher'] = higher

    romantic = request.POST.get('romantic')
    context['romantic'] = romantic

    activities = request.POST.get('activities')
    context['activities'] = activities

    Walc = request.POST.get('Walc')
    context['Walc'] = Walc

    failures = request.POST.get('failures')
    context['failures'] = failures

    G1 = request.POST.get('G1')
    context['G1'] = G1

    G1_val = int(G1)

    G2 = request.POST.get('G2')
    context['G2'] = G2

    G2_val = int(G2)

    G3 = request.POST.get('G3')
    context['G3'] = G3

    G3_val = int(G3)

    learning = request.POST.get('learning')
    personal = request.POST.get('personal')
    area = request.POST.get('area')

    # assestment =  do_classify(context)
    # context['assestment'] = assestment
    # print(assestment)

    total = G1_val + G2_val + G3_val

    if total >= 30:
        assestment = "Pass"
    else:
        assestment = "Fail"



    data = Students.objects.all()
    data = Students(id=stid, first_name=fname, last_name=lname, student_id=stid, gender=sex, age=age,
                    parental_status=Pstatus, guardian=guardian, intention=higher, romantic=romantic,
                    extra_curr=activities, alcohol_cons=Walc, no_of_failures=failures, grade1=G1, grade2=G2, grade3=G3,
                    result=assestment)
    data.save()
    mystudent = Students.objects.get(id=stid)

    if total > 30:
        mydata = Pass.objects.all()
        mydata = Pass(student=mystudent, learning_styles=learning, personality_styles=personal, area_of_interests=area)
        mydata.save()
    else:
        mydata = Fail.objects.all()
        mydata = Fail(student=mystudent, learning_styles=learning, personality_styles=personal, area_of_interests=area)
        mydata.save()

    contest = {
        'mystudent': mystudent,
        'assestment': assestment
    }
    return render(request, 'match/predictdisplay.html', contest)


def exit(request):
    context = {}
    return render(request, 'match/exit.html', context)
