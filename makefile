all: out/people.html

out/people.html: main.py templates/people.html
	python main.py

clean:
	rm -f *~ templates/*~ out/*~

cleaner: clean
	rm -f out/*.html
