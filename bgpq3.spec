Name:           bgpq3
Version:        0.1.28
Release:        0%{?dist}

Group:          System/Utilities
Summary:        Automate BGP filter generation based on routing database information
URL:            http://snar.spb.ru/prog/bgpq3/
License:        BSD
Source0:        http://snar.spb.ru/prog/bgpq3/bgpq3-0.1.28.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
You are running BGP in your network and want to automate filter generation for your routers? Well, with BGPQ3 it's easy.

%prep
%setup -q

%build
./configure --prefix=$RPM_BUILD_ROOT%{_prefix} --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/bin/bgpq3
/usr/man/man8/bgpq3.8.gz
%doc COPYRIGHT CHANGES


%changelog
* Tue Mar 10 Alexandre Snarskii <snar@snar.spb.ru> 0.1.28
- Version updated

* Wed Oct 29 Alexandre Snarskii <snar@snar.spb.ru> 0.1.25
- Version updated

* Thu Jun 5 2014 Alexandre Snarskii <snar@snar.spb.ru> 0.1.21-0.snar
- Version updated

* Thu May 9 2013 Alexandre Snarskii <snar@snar.spb.ru> 0.1.19-0.snar
- Version updated

* Sun Feb 24 2013 Alexandre Snarskii <snar@snar.spb.ru> 0.1.18-3.snar
- License corrected

* Wed Feb 20 2013 Arnoud Vermeer <arnoud@tumblr.com> 0.1.18-2.tumblr
- Adding missing group info (arnoud@tumblr.com)

* Wed Feb 20 2013 Arnoud Vermeer <arnoud@tumblr.com> 0.1.18-1.tumblr
- new package built with tito
