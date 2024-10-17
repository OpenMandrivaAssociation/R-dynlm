%global packname  dynlm
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.3.2
Release:          1
Summary:          Dynamic Linear Regression
Group:            Sciences/Mathematics
License:          GPL-2
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/dynlm_0.3-2.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-stats R-zoo R-lmtest R-car 
Requires:         R-stats R-strucchange 
Requires:         R-datasets R-sandwich R-strucchange R-TSA 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats R-zoo R-lmtest R-car
BuildRequires:    R-stats R-strucchange 
BuildRequires:    R-datasets R-sandwich R-strucchange R-TSA 

%description
Dynamic linear models and time series regression.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
