CC = python3.7
CFLAGS= -m mwb

TARGET = output

.PHONY: clean FORCE

all: $(TARGET)

# output: website.yaml pages/ placeholder/ static/ themes/
output: FORCE
	rm -rf $@
	$(CC) $(CFLAGS) . $@
# 	chmod -R +x $@

clean:
	rm -rf $(TARGET)

FORCE: