%define		template	varnish
Summary:	Varnish Cache statistics template for Cacti
Name:		cacti-template-%{template}
Version:	5
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/glensc/cacti-template-varnish/archive/v%{version}/%{template}-%{version}.tar.gz
# Source0-md5:	3ff32e25c6ea52ca46f4eda4139ea400
URL:		https://github.com/glensc/cacti-template-varnish
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.554
Requires:	cacti >= 0.8.7e-8
Conflicts:	cacti-spine < 0.8.7e-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		resourcedir		%{cactidir}/resource
%define		scriptsdir		%{cactidir}/scripts

%description
Template for Cacti - Varnish Cache statistics.

%prep
%setup -qc
mv cacti-template-varnish-*/* -v .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{resourcedir},%{scriptsdir}}
install -p get_varnish_stats.py $RPM_BUILD_ROOT%{scriptsdir}
cp -p *.xml $RPM_BUILD_ROOT%{resourcedir}

%post
%cacti_import_template %{resourcedir}/cacti_host_template_varnish.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{scriptsdir}/get_varnish_stats.py
%{resourcedir}/*.xml
