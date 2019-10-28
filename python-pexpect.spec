#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_with	tests	# py.test tests [require ptys, so not on builders]
%bcond_without	doc	# Sphinx documentation

%define		module	pexpect
Summary:	Pure Python Expect-like module
Summary(pl.UTF-8):	Moduł podobny do narzędzia Expect napisany w czystym Pythonie
Name:		python-%{module}
Version:	4.7.0
Release:	2
License:	ISC
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/pexpect/
Source0:	https://files.pythonhosted.org/packages/source/p/pexpect/pexpect-%{version}.tar.gz
# Source0-md5:	ed003242cbf308aee1b1eaecdef59e43
URL:		http://pexpect.readthedocs.io/
%if %{with tests} && %(locale -a | grep -q '^C\.utf8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
%if %{with tests}
BuildRequires:	python-ptyprocess >= 0.5
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
%if %{with tests}
BuildRequires:	python3-ptyprocess >= 0.5
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.7
Requires:	python-ptyprocess >= 0.5
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

%package -n python3-%{module}
Summary:	Pure Python Expect-like module
Summary(pl.UTF-8):	Moduł podobny do narzędzia Expect napisany w czystym Pythonie
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.2
Requires:	python3-ptyprocess >= 0.5

%description -n python3-%{module}
Pexpect is a pure Python module for spawning child applications;
controlling them; and responding to expected patterns in their output.
Pexpect works like Don Libes' Expect. Pexpect allows your script to
spawn a child application and control it as if a human were typing
commands.

%description -n python3-%{module} -l pl.UTF-8
Pexpect jest modułem napisanym wyłącznie w Pythonie przeznaczonym do
uruchamiania aplikacji i kontroli nad nimi poprzez reagowanie na
znalezione wzorce na ich wyjściu. Pexpect działa podobnie do Expecta
Dona Libesa - pozwala skryptom z ich poziomu uruchomić inne programy i
sprawować nad nimi kontrolę imitując interakcję użytkownika.

%package apidocs
Summary:	Documentation for Python pexpect module
Summary(pl.UTF-8):	Dokumentacja do modułu Pythona pexpect
Group:		Documentation

%description apidocs
Documentation for Python pexpect module.

%description apidocs -l pl.UTF-8
Dokumentacja do modułu Pythona pexpect.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%{?with_tests:LC_ALL=C.UTF-8 %{__python} -m pytest tests}
%endif

%if %{with python3}
%py3_build

%{?with_tests:LC_ALL=C.UTF-8 %{__python3} -m pytest tests}
%endif

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/pexpect/bashrc.sh

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/pexpect/bashrc.sh

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/pexpect
%{py_sitescriptdir}/pexpect-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/pexpect
%{py3_sitescriptdir}/pexpect-%{version}-py*.egg-info
%{_examplesdir}/python3-%{module}-%{version}
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/{_static,api,*.html,*.js}
%endif
