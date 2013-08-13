
VERSION=0.2
ARCH=noarch
PACKAGE=amahi-netboot
RPMBUILDDIR= $(HOME)/rpmbuild

rpm: update-header dist
	(cd release && rpmbuild -ta $(PACKAGE)-$(VERSION).tar.gz)
	mv $(RPMBUILDDIR)/RPMS/$(ARCH)/$(PACKAGE)-$(VERSION)-*.$(ARCH).rpm release/
	mv $(RPMBUILDDIR)/SRPMS/$(PACKAGE)-$(VERSION)-*.src.rpm release/

dist:
	(mkdir -p release && cd release && mkdir -p $(PACKAGE)-$(VERSION))
	rsync -Ca $(PACKAGE).spec Makefile tftp amahi-pxe.conf release/$(PACKAGE)-$(VERSION)/
	(cd release && tar -czvf $(PACKAGE)-$(VERSION).tar.gz $(PACKAGE)-$(VERSION))
	(cd release && rm -rf $(PACKAGE)-$(VERSION))

update-header:
	sed -i -e 's/^Version:\s*[0-9.]*\s*$$/Version: $(VERSION)/' $(PACKAGE).spec

install: rpm
	(cd release && sudo rpm -Uvh $(PACKAGE)-$(VERSION)-*.$(ARCH).rpm)

