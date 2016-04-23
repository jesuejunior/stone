FROM jesuejunior/python:3

COPY . /stone

WORKDIR /stone

RUN pip install -r requirements.txt \
	&& python3 manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "--log-file", "/var/log/stone.error.log",  "-w", "2", "stone.wsgi:application"]
