#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : can-utils
Version  : 2018.02.0
Release  : 1
URL      : https://github.com/linux-can/can-utils/archive/v2018.02.0.tar.gz
Source0  : https://github.com/linux-can/can-utils/archive/v2018.02.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: can-utils-bin = %{version}-%{release}

%description
<p align="center">
<img src="https://github.com/linux-can/can-logos/raw/master/png/SocketCAN-logo-60dpi.png" alt="SocketCAN logo"/>
</p>

%package bin
Summary: bin components for the can-utils package.
Group: Binaries

%description bin
bin components for the can-utils package.


%prep
%setup -q -n can-utils-2018.02.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556029424
export LDFLAGS="${LDFLAGS} -fno-lto"
%autogen --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1556029424
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/asc2log
/usr/bin/bcmserver
/usr/bin/can-calc-bit-timing
/usr/bin/canbusload
/usr/bin/candump
/usr/bin/canfdtest
/usr/bin/cangen
/usr/bin/cangw
/usr/bin/canlogserver
/usr/bin/canplayer
/usr/bin/cansend
/usr/bin/cansniffer
/usr/bin/isotpdump
/usr/bin/isotpperf
/usr/bin/isotprecv
/usr/bin/isotpsend
/usr/bin/isotpserver
/usr/bin/isotpsniffer
/usr/bin/isotptun
/usr/bin/jacd
/usr/bin/jspy
/usr/bin/jsr
/usr/bin/log2asc
/usr/bin/log2long
/usr/bin/slcan_attach
/usr/bin/slcand
/usr/bin/slcanpty
/usr/bin/testj1939
