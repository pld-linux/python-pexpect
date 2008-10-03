%define		module	pexpect
Summary:	Expect module for Python
Summary(pl.UTF-8):	Moduł Pythona automatyzujący zadania, wzorowany na Expect
Name:		python-%{module}
Version:	2.3
Release:	2
License:	PSF
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pexpect/pexpect-%{version}.tar.gz
# Source0-md5:	bf107cf54e67bc6dec5bea1f3e6a65c3
URL:		http://pexpect.sourceforge.net/
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pexpect is a pure Python module for spawning child applications;
controlling them; and responding to expected patterns in their output.
Pexpect works like Don Libes' Expect. Pexpect allows your script to
spawn a child application and control it as if a human were typing
commands.

%description -l pl.UTF-8
Pexpect jest modułem napisanym wyłącznie w Pythonie przeznaczonym do
uruchamiania aplikacji i kontroli nad nimi poprzez reagowanie na
znalezione wzorce na ich wyjściu. Pexpect działa podobnie do Expecta
Dona Libesa - pozwala skryptom z ich poziomu uruchomić inne programy i
sprawować nad nimi kontrolę imitując interakcję użytkownika.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

install examples/*.py {ANSI,FSM,screen}.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*.html
%{py_sitescriptdir}/*.py[co]
%{_examplesdir}/%{name}-%{version}
