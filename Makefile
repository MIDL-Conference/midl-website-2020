CC = python3
CFLAGS = -m mwb

DEBUG = --prettify

TARGET = /usr/share/nginx/midl

HOST = beta.2020.midl.io:
PORT = 484

.PHONY: clean generate deploy FORCE

all: generate $(TARGET)


generate: pages/program/papers/paper.template papers.json
	$(CC) generate_papers.py $^ pages/program/

pages/program/full-papers.md: pages/program/full-papers.template papers.json
	$(CC) fill_template.py $^ full $@
pages/program/short-papers.md: pages/program/short-papers.template papers.json
	$(CC) fill_template.py $^ short $@

$(TARGET): FORCE pages/program/full-papers.md pages/program/short-papers.md
	rm -rf $@
	$(CC) $(CFLAGS) . $@ $(DEBUG)
# 	chmod -R +x $@

deploy:
	scp -r -P $(PORT) $(TARGET) $(HOST)

clean:
	rm -rf $(TARGET)

FORCE: