CC = python3
CFLAGS = -m mwb

DEBUG = --prettify

TARGET = /usr/share/nginx/midl

HOST = beta.2020.midl.io:
PORT = 484

.PHONY: clean generate deploy FORCE

all: generate $(TARGET)


generate: pages/papers/paper.template papers.json
	$(CC) generate_papers.py $^ pages/

# pages/program/full-papers.md: pages/program/full-papers.template papers.json
# 	$(CC) fill_template.py $^ full $@
# pages/program/short-papers.md: pages/program/short-papers.template papers.json
# 	$(CC) fill_template.py $^ short $@
pages/scientific-program.md: pages/scientific-program.template papers.json
	$(CC) fill_template.py $^ $@

$(TARGET): FORCE pages/scientific-program.md
	rm -rf $@
	$(CC) $(CFLAGS) . $@ $(DEBUG)
# 	chmod -R +x $@

deploy:
	scp -r -P $(PORT) $(TARGET) $(HOST)

clean:
	rm -rf $(TARGET)

FORCE: