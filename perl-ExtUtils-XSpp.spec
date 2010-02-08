%define upstream_name    ExtUtils-XSpp
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A tiny C++ class example that holds a string and an int
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/ExtUtils/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Base)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Module::Build)
BuildRequires: perl-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Provides: perl(ExtUtils::XSpp::Lexer)

%description
Anything that does not look like a XS++ directive or a class declaration is
passed verbatim to XS. If you want XS++ to ignore code that looks like a
XS++ directive or class declaration, simply surround it with a raw block
delimiter like this:

  %{
  XS++ won't interpret this
  %}

%code
    See under *Classes*.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/xspp
/usr/share/man/man1/xspp.1.lzma

