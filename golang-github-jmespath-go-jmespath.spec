# http://github.com/jmespath/go-jmespath
%global goipath         github.com/jmespath/go-jmespath
%global commit          c2b33e8439af944379acbdd9c3a5fe0bc44bd8a5

%gometa

Name:           golang-github-jmespath-go-jmespath
Version:        0.2.2
Release:        0.10%{?dist}
Summary:        Golang implementation of JMESPath
# Detected licences
# - Apache (v2.0) at 'LICENSE'
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

# Tests deps
BuildRequires: golang(github.com/stretchr/testify/assert)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
# /usr/bin/ld: cannot find /usr/lib64/libpthread_nonshared.a
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org>
- 0.2.2-0.10
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Oct 05 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.2-0.9.20181005gitbd40a43
- Bump to upstream c2b33e8439af944379acbdd9c3a5fe0bc44bd8a5

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-0.8.gitbd40a43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.2.2-0.7.gitbd40a43
- Upload glide files

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.2.2-0.6.20160803gitbd40a43
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-0.5.gitbd40a43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-0.4.gitbd40a43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-0.3.gitbd40a43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-0.2.gitbd40a43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.2.2-0.1.gitbd40a43
- Bump to upstream bd40a432e4c76585ef6b72d3fd96fb9b6dc7b68d
  resolves: #1413287

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git0b12d6b
- https://fedoraproject.org/wiki/Changes/golang1.7

* Fri Apr 15 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git0b12d6b
- First package for Fedora
  resolves: #1297550
