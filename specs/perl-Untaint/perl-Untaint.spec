# $Id$
# Authority: dag
# Upstream: Kevin Meltzer <kmeltz$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Untaint

Summary: Perl module for laundering tainted data
Name: perl-Untaint
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Untaint/

Source: http://www.cpan.org/authors/id/K/KM/KMELTZ/Untaint-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Untaint is a Perl module for laundering tainted data.

This package contains the following Perl module:

    Untaint

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/Untaint.3pm*
%{perl_vendorlib}/untaint_array_t.pl
%{perl_vendorlib}/untaint_hash_t.pl
%{perl_vendorlib}/untaint_scalar_t.pl
%{perl_vendorlib}/Untaint.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
