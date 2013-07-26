%define upstream_name    ExtUtils-XSpp
%define upstream_version 0.1602

%define debug_package %{nil}

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A tiny C++ class example that holds a string and an int
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Digest::MD5) >= 2.0.0
BuildRequires:	perl(ExtUtils::ParseXS) >= 2.220.200
BuildRequires:	perl(Module::Build) >= 0.380.0
BuildRequires:	perl(Test::Base)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl-devel
Requires:	perl(ExtUtils::ParseXS) >= 2.220.0
Provides:	perl(ExtUtils::XSpp::Lexer)

%description
Anything that does not look like a XS++ directive or a class declaration is
passed verbatim to XS.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes META.json META.yml README examples
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*

