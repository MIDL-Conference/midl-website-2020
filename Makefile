CC = python3
CFLAGS = -m mwb

DEBUG = --prettify

TARGET = output

.PHONY: clean FORCE

all: $(TARGET)

# output: website.yaml pages/ placeholder/ static/ themes/
output: FORCE
	rm -rf $@
	$(CC) $(CFLAGS) . $@ $(DEBUG)
# 	chmod -R +x $@

clean:
	rm -rf $(TARGET)

FORCE: