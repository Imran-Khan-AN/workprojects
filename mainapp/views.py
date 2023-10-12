
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# from langchain.document_loaders import PyPDFLoader
import tempfile
import os
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import SKLearnVectorStore


# @login_required(login_url='/login')
def document_analysis(request):
    return render(request, 'document_analysis.html')

def index(request):
    return render(request, 'home.html')

@login_required(login_url='/login')
def audio(request):
    return render(request, 'audio.html')


@login_required(login_url='/login')
def document(request):
    return render(request, 'document.html')


def process_and_store_docs(docs,filename):
    # embeddingss =  OpenAIEmbeddings()
    # persist_path = os.path.join("./", f"union.parquet")
    # print(persist_path)
    # vector_store = SKLearnVectorStore.from_documents(
    #     documents=docs,
    #     embedding=embeddingss,
    #     persist_path=persist_path,  # persist_path and serializer are optional
    #     serializer="parquet",
    # )
    # vector_store.persist()
    # print("Vector store was persisted to", persist_path)
    pass

def split_docs(documents, chunk_size=1000, chunk_overlap=20):
    # from langchain.text_splitter import RecursiveCharacterTextSplitter
    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    # docs = text_splitter.split_documents(documents)
    # return docs
    pass

def temp_file_maker(file):
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    for chunk in file.chunks():
        temp_file.write(chunk)
    temp_file.close()
    return temp_file


def handle_pdf_file(file):
    # print("i am in pdf")
    # temp_file = temp_file_maker(file)
    # loader = PyPDFLoader(temp_file.name)
    # documents = loader.load()
    # docs = split_docs(documents)
    # process_and_store_docs(docs,file.name)
    # return documents
    pass


def handle_doc_file(file):
    # temp_file = temp_file_maker(file)
    # from langchain.document_loaders import Docx2txtLoader
    # loader = Docx2txtLoader(temp_file.name)
    # documents = loader.load()
    # docs = split_docs(documents)
    # process_and_store_docs(docs,file.name)
    # return documents
    pass



@login_required(login_url='/login')
@csrf_exempt
def document_upload_view(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']

        try:
            if file:
                # Split the filename on . to get the extension and handle it accordingly
                ext = file.name.split('.')[-1].lower()

                if ext == 'pdf':
                    doc = handle_pdf_file(file)
                elif ext == 'doc' or ext == 'docx':
                    doc = handle_doc_file(file)
                else:
                    # Return a response if the file type isn't supported
                    return JsonResponse({'status':'error','message': f'File type .{ext} not supported!'}, status=200)
                
            content = ""

            for document in doc:
                content += f"{document.page_content}"

            print(doc[0].page_content)
            
            return JsonResponse({'message':'success' , 'text': content}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'status':'error' }, status=400)
        

        return JsonResponse({"message": "File uploaded successfully!"})
    
    return JsonResponse({"message": "Invalid request"})




@login_required(login_url='/login')
def upload_file(request):
    return render(request, 'chatbot.html')


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/login')
@csrf_exempt
def upload_audio(request):
    if request.method == 'POST':
        # Get the uploaded file
        audio_file = request.FILES['audioFile']

        # TODO: Process the file
        # This will depend on what you need to do with the file

        # Return a response
        return JsonResponse({'success': True, 'message': '''Customer: Good morning, I'm interested in opening a savings account with your bank. I've heard about some
promotional offers, and I would like to know more about them.
Bank Representative: Good morningl Absolutely, we have some exciting promotional offers available for our new
customers. One of our exclusive offers is the "Guaranteed 10% Annual Interest Account."
Customer: That sounds too good to be true. Are you sure it guarantees a 10% annual interest rate?
Bank Representative: Absolutelyl Our Guaranteed 10% Annual Interest Account is an exceptional opportunity for our
valued customers. You can enjoy a fixed 10% interest rate on your savings, which is guaranteed for the entire
duration of the account.''', 'audio_file': f'{str(audio_file)}'})

    return JsonResponse({'success': False, 'message': 'Invalid request'})




@login_required(login_url='/login')
@csrf_exempt
def document_analysis_api(request):
    if request.method == 'POST':
        # Get the uploaded file
        files = request.FILES

        print(files)
        # TODO: Process the file
        # This will depend on what you need to do with the file

        # Return a response
        return JsonResponse({'success': True, 'message': '''3. Roles and Responsibilities - Internal
            Audit:
            Text 1: Internal Audit is responsible
            for verifying all the processes
            undertaken during the model
            lifecycle, including independent
            evaluation/assessment of the first
            two lines of defense.
            Text 2: Internal Audit is responsible
            for verifying all the processes
            undertaken during the model
            lifecycle, including independent
            validation of the models.'''},)

    return JsonResponse({'success': False, 'message': 'Invalid request'})


def reg(request):
    if request.method == 'POST':
        # Handle file upload if needed, but you mentioned it's random so maybe just discard it

        with open('reg_json.txt', 'r') as file:
            reg_json_content = file.read()
            
        with open('reg_html.txt', 'r') as file:
            reg_html_content = file.read()

        return JsonResponse({'reg_json': reg_json_content, 'reg_html': reg_html_content})

    return render(request, 'reg_as_code.html')


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import json

openai.api_key = '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'


@login_required(login_url='/login')
@csrf_exempt
def ask_document(request):
    if request.method == 'POST':
        
        # embeddings =  OpenAIEmbeddings()
        # persist_path = os.path.join("./", "union.parquet")

        # data = json.loads(request.body)
        # user_message = data.get('message')
        # thread_id = data.get('thread_id')

        

        # vector_store2 = SKLearnVectorStore(
        #     embedding=embeddings, persist_path=persist_path, serializer="parquet"
        # )
        # print("read the store")
        # from langchain.chat_models import ChatOpenAI
        # model_name = "gpt-3.5-turbo"
        # llm = ChatOpenAI(model_name=model_name)

        # from langchain.llms import OpenAI
        # from langchain.chains import ConversationalRetrievalChain
        # from langchain.memory import ConversationBufferMemory ,ConversationSummaryMemory

        # connection_string = "mongodb://127.0.0.1:27017"
        # from langchain.memory import MongoDBChatMessageHistory

       
        # memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True,)


        # qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0), vector_store2.as_retriever(), memory=memory)
        
        # result = qa({"question": user_message})


        # vector_store_retriever = vector_store2.as_retriever()

        # relevant_documents = vector_store_retriever.get_relevant_documents("Capital Assets Guidlines.pdf")

        # print(relevant_documents[0].metadata['id'])


        # doc_to_delete = relevant_documents[0]

        

        # bot_message = result["answer"]

        bot_message = bot_message
        return JsonResponse({'message': bot_message})




@login_required(login_url='/login')
@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message')

        # Generate a response using the OpenAI API


        import os
        import openai
        openai.api_type = "azure"
        openai.api_base = "https://genie-aoai.openai.azure.com/"
        openai.api_version = "2023-07-01-preview"
        openai.api_key = 'ed09f545896a47f090f4a880268ac988'

        response = openai.ChatCompletion.create(
        engine="gpt35turbo",
        messages = [{"role":"system","content":"You are an AI assistant that helps people find information."},
                   {"role": "user", "content": user_message},],

        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)

        bot_message = response['choices'][0]['message']['content']




        return JsonResponse({'message': bot_message})



from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login

from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/chat_zone')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/chat_zone')  # Replace '/' with the appropriate URL for your home page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/chat_zone')
    

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully created an account for {username}.')
            return redirect('/login')  # Replace '/' with the appropriate URL for your home page
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()}: {error}')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    # os.remove(os.path.join("./", "union.parquet"))
    return redirect('/')  # Replace 'login' with the name of your login page URL



