%define major %(echo %{version} |cut -d. -f1)
%define libname %mklibname z3 %{major}
%define devname %mklibname z3 -d

Name:		z3
Version:	4.12.2
Release:	1
Summary:	The Z3 Theorem Prover
Source0:	https://github.com/Z3Prover/z3/archive/z3-z3-%{version}.tar.gz
License:	MIT
Requires:	%{libname} = %{EVRD}
BuildRequires:	cmake
BuildRequires:	ninja

%description
Z3 Theorem Prover is a satisfiability modulo theories (SMT) solver.

Z3 supports arithmetic, fixed-size bit-vectors, extensional arrays,
datatypes, uninterpreted functions, and quantifiers. Its main
applications are extended static checking, test case generation,
and predicate abstraction.

%package -n %{libname}
Summary:	Library for the Z3 Theorem Prover
Group:		System/Libraries

%description -n %{libname}
Library for the Z3 Theorem Prover

%package -n %{devname}
Summary:	Development files for the Z3 Theorem Prover
Group:		Development/C

%description -n %{devname}
Development files for the Z3 Theorem Prover

%prep
%autosetup -p1 -n z3-z3-%{version}
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/z3

%files -n %{libname}
%{_libdir}/libz3.so.%{major}*

%files -n %{devname}
%{_libdir}/libz3.so
%{_includedir}/*.h
%{_libdir}/cmake/z3
%{_libdir}/pkgconfig/z3.pc
