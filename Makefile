CC = python3
CFLAGS = -m mwb

DEBUG = --prettify

TARGET = output

.PHONY: clean FORCE

all: $(TARGET)

pages/program/full-papers.md: pages/program/full-papers.template papers.json
	$(CC) fill_template.py $^ full $@
pages/program/short-papers.md: pages/program/short-papers.template papers.json
	$(CC) fill_template.py $^ short $@

$(TARGET): FORCE pages/program/full-papers.md pages/program/short-papers.md
	rm -rf $@
	$(CC) $(CFLAGS) . $@ $(DEBUG)
# 	chmod -R +x $@

clean:
	rm -rf $(TARGET)

FORCE: