%define		module	pexpect
Summary:	Expect module for Python
Summary(pl):	Modu³ Pythona automatyzuj±cy zadania, wzorowany na Expect
Name:		python-%{module}
Version:	0.999
Release:	0.1
License:	PSF
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pexpect/%{module}-%{version}.tgz
# Source0-md5:	e426e5f54d323aaf392008c9eb35131d
Source1:	http://dl.sourceforge.net/pexpect/%{module}-doc.tgz
# Source1-md5:	69bfc0056938f561875289651c8715ad
Source2:	http://dl.sourceforge.net/pexpect/%{module}-examples.tgz
# Source2-md5:	ee05cad1d7b6b4de0dc74bc16330b852
URL:		http://pexpect.soufceforge.net/
BuildRequires:	python-modules
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pexpect is a pure Python module for spawning child applications;
controlling them; and responding to expected patterns in their output.
Pexpect works like Don Libes' Expect. Pexpect allows your script to
spawn a child application and control it as if a human were typing
commands.

%description -l pl
Pexpect jest modu³em napisanym wy³±cznie w Pythonie przeznaczonym do
uruchamiania aplikacji i kontroli nad nimi poprzez reagowanie na
znalezione wzorce na ich wyj¶ciu. Pexpect dzia³a podobnie do Expecta
Dona Libesa - pozwala skryptom z ich poziomu uruchomiæ inne programy i
sprawowaæ nad nimi kontrolê imituj±c interakcjê u¿ytkownika.

%prep
%setup -q -n %{module}-%{version} -a 1 -a 2

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT

install examples/*.py {ANSI,FSM,screen}.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc/*.html
%{py_sitescriptdir}/*.py[co]
%{_examplesdir}/%{name}-%{version}
