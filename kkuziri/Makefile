SUBDIRS = models templates views

clean :
	@rm -f *.pyc .*.swp
	@for d in $(SUBDIRS); do (cd $$d; make clean ); done
