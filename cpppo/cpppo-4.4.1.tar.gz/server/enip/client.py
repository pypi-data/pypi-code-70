
# 
# Cpppo -- Communication Protocol Python Parser and Originator
# 
# Copyright (c) 2013, Hard Consulting Corporation.
# 
# Cpppo is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.  See the LICENSE file at the top of the source tree.
# 
# Cpppo is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# 

from __future__ import absolute_import, print_function, division
try:
    from future_builtins import zip, map # Use Python 3 "lazy" zip, map
except ImportError:
    pass

__author__                      = "Perry Kundert"
__email__                       = "perry@hardconsulting.com"
__copyright__                   = "Copyright (c) 2013 Hard Consulting Corporation"
__license__                     = "Dual License: GPLv3 (or later) and Commercial (see LICENSE)"

__all__				= ['parse_int', 'parse_path', 'parse_path_elements', 'parse_path_component',
                                   'format_path', 'format_context', 'parse_context', 'CIP_TYPES', 'parse_operations',
                                   'client', 'await_response', 'connector', 'recycle', 'main', 'ENIPStatusError' ]


"""enip.client	-- EtherNet/IP client API and module entry point

    A high-thruput pipelining API for accessing EtherNet/IP CIP Controller data via Tags or
Class/Instance/Attribute numbers.

    Module entry point process tags specified on the command-line and/or from stdin (if '-'
specified).  Optionally prints results (if --print specified).

"""

import argparse
import array
import collections
import contextlib
import csv
import itertools
import json
import logging
import random
import select
import socket
import sys
import traceback
import warnings

from ... import misc
from ...dotdict import dotdict
from ...automata import ( log_cfg, type_str_base, chainable, peekable )
from .. import network
from . import defaults, parser, device

# used to be defined here; retain for backward-compatibility...
def parse_int( *args, **kwds ):
    return device.parse_int( *args, **kwds )
def parse_path( *args, **kwds ):
    return device.parse_path( *args, **kwds )
def parse_path_elements( *args, **kwds ):
    return device.parse_path_elements( *args, **kwds )
def parse_path_component( *args, **kwds ):
    return device.parse_path_component( *args, **kwds )

log				= logging.getLogger( "enip.cli" )

class ENIPStatusError( Exception ):
    def __init__(self, status=None):
        self.status		= status
        super( ENIPStatusError, self ).__init__("Response EtherNet/IP status: %d" % ( status ))


def format_path( segments, count=None ):
    """Format some simple path segment lists in a human-readable form.  Raises an Exception if
    unrecognized (only [{'symbolic': <tag>}, ...] or [{'class': ...}, {'instance': ...},
    {'attribute': ...}, ...] paths are handled, optionally followed by an {'element': ...}.

    If an 'element' segment is provided, we'll append a [#] element index; if count is also provided
    we'll append a [#-#] element range.

    """
    if isinstance( segments, type_str_base ):
        path			= segments
    else:
        symbolic		= ''
        numeric			= []
        element			= None
        for seg in segments:
            if 'symbolic' in seg:
                symbolic       += ( '.' if symbolic else '' ) + seg['symbolic']
            elif 'class' in seg and len( numeric ) == 0:
                numeric.append( "0x%04X" % seg['class'] )
            elif 'instance' in seg and len( numeric ) == 1:
                numeric.append( "%d" % seg['instance'] )
            elif 'attribute' in seg and len( numeric ) == 2:
                numeric.append( "%d" % seg['attribute'] )
            elif 'element' in seg:
                element		= seg['element']
            else:
                numeric.append( json.dumps( seg, separators=(',',':')))
            assert bool( symbolic ) ^ bool( numeric ), \
                "Unformattable path segment: %r" % seg
        path			= symbolic if symbolic else ('@' + '/'.join( numeric ))

        if element is not None:
            if count is not None:
                path	       += "[%d-%d]" % ( element, element + count - 1 )
            else:
                path	       += "[%d]" % ( element )
    log.detail( "Formatted %32s from: %s", path, segments )
    return path


def format_context( sender_context ):
    """Produce a sender_context bytearray of exactly length 8, NUL-padding on the right."""
    assert isinstance( sender_context, (bytes,bytearray,array.array) ), \
        "Expected sender_context of bytes/bytearray/array, not %r" % sender_context
    return bytearray( sender_context[:8] ).ljust( 8, b'\0' )


def parse_context( sender_context ):
    """Restore a bytes string from a bytearray sender_context, stripping any NUL padding on the
    right."""
    assert isinstance( sender_context, (bytes,bytearray,array.array) ), \
        "Expected sender_context of bytes/bytearray/array, not %r" % sender_context
    return bytes( bytearray( sender_context ).rstrip( b'\0' ))


# 
# client.CIP_TYPES
# 
#     The supported CIP data types, and their CIP 'tag_type' values, byte sizes and validators.  We
# are generous with the "signed" types (eg. SINT, INT, DINT, LINT), and we actually allow the full
# unsigned range, plus the negative range.  There is little risk to doing this, as all provided
# values will fit legitimately into the data type without loss.  It does however, make acceptance of
# automatically generated data easier, as we don't need to really know if the data is signed or
# unsigned; just that it fits into the target data type.
# 

def int_validate( x, lo, hi ):
    res			= int( x )
    assert lo <= res <= hi, "Invalid %d; not in range (%d,%d)" % ( res, lo, hi)
    return res

def bool_validate( b ):
    try:
        res		= int( b ) != 0
        return res
    except ValueError:
        pass
    lowered = b.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    raise ValueError("Invalid %s; could not be interpreted as boolean" % b)

CIP_TYPES			= {
    'STRING':	(parser.STRING.tag_type, 0,				str ),
    'SSTRING':	(parser.SSTRING.tag_type, 0,				str ),
    'BOOL':	(parser.BOOL.tag_type,	parser.BOOL.struct_calcsize,	bool_validate ),
    'REAL': 	(parser.REAL.tag_type,	parser.REAL.struct_calcsize,	float ),
    'LREAL': 	(parser.LREAL.tag_type,	parser.LREAL.struct_calcsize,	float ),
    'LINT':	(parser.LINT.tag_type,	parser.LINT.struct_calcsize,	lambda x: int_validate( x, -2**63, 2**64-1 )), # extra range
    'ULINT':	(parser.ULINT.tag_type,	parser.ULINT.struct_calcsize,	lambda x: int_validate( x,  0,     2**64-1 )),
    'DINT':	(parser.DINT.tag_type,	parser.DINT.struct_calcsize,	lambda x: int_validate( x, -2**31, 2**32-1 )), # extra range
    'UDINT':	(parser.UDINT.tag_type,	parser.UDINT.struct_calcsize,	lambda x: int_validate( x,  0,     2**32-1 )),
    'INT':	(parser.INT.tag_type,	parser.INT.struct_calcsize,	lambda x: int_validate( x, -2**15, 2**16-1 )), # extra range
    'UINT':	(parser.UINT.tag_type,	parser.UINT.struct_calcsize,	lambda x: int_validate( x,  0,     2**16-1 )),
    'SINT':	(parser.SINT.tag_type,	parser.SINT.struct_calcsize,	lambda x: int_validate( x, -2**7,  2**8-1 )),  # extra range
    'USINT':	(parser.USINT.tag_type,	parser.USINT.struct_calcsize,	lambda x: int_validate( x,  0,     2**8-1 )),
}

def parse_operations( tags, fragment=False, int_type=None, **kwds ):
    """Given a sequence of (string) tags, deduce the set of I/O desired operations, yielding each one.
    If a dict is seen, it is passed through.  Any additional keyword parameters are added to each
    operation (eg. route_path = [{'link':0,'port':0}])

    Parse each EtherNet/IP Tag Read or Write; only write operations will have 'data'; default
    'method' is considered 'read':

        TAG	 		read 1 value (no element index)
        TAG[0]	 		read 1 value from element index 0
        TAG[1-5]		read 5 values from element indices 1 to 5
        TAG[1-5]+4		read 5 values from element indices 1 to 5, beginning at byte offset 4
        TAG[4-7]=1,2,3,4	write 4 values from indices 4 to 7
        @0x1FF/01/0x1A[99]	read the 100th element of class 511/0x1ff, instance 1, attribute 26

    To support access to scalar attributes (no element index allowed in path), we cannot default to
    supply an element index of 0; default is no element in path, and a data value count of 1.  If a
    byte offset is specified, the request is forced to use Read/Write Tag Fragmented.

    Default CIP int_type for int data (data with no '.' in it, by default) is CIP 'INT'.

    """
    if int_type is None:
        int_type		= 'INT'
    for tag in tags:
        # Pass-thru (already parsed) operation?
        if isinstance( tag, dict ):
            tag.update( kwds )
            yield tag
            continue

        # Compute tag (stripping val and off), discarding whitespace around tag and val/off.
        val			= ''
        opr			= {}
        if '=' in tag:
            # A write; strip off the values into 'val'
            tag,val		= [s.strip() for s in tag.split( '=', 1 )]
            opr['method']	= 'write'

        if '+' in tag:
            # A byte offset (valid for Fragmented)
            tag,off		= [s.strip() for s in tag.split( '+', 1 )]
            if off:
                opr['offset']	= int( off )

        # If a count of elements is defined, save it; Otherwise, deduce it from values (write_tag),
        # or leave it unset and use the method default (usually 1) if necessary (read_tag/frag)
        seg,elm,cnt		= device.parse_path_elements( tag )
        opr['path']		= seg
        if cnt is not None:
            opr['elements']	= cnt

        if val:
            # Default between REAL/INT, by simply checking for '.' in the provided value(s)
            if '.' in val:
                opr['tag_type'],size,cast = CIP_TYPES['REAL']
            else:
                opr['tag_type'],size,cast = CIP_TYPES[int_type.strip().upper()]
            # Allow an optional (TYPE)value,value,...
            if val.strip().startswith( '(' ) and ')' in val:
                typ,val		= val.split( ')', 1 ) # Get leading: ['(TYPE', '), ...]
                _,typ		= typ.split( '(', 1 )
                opr['tag_type'],size,cast = CIP_TYPES[typ.strip().upper()]

            # The provided val is a comma-separated, whitespace-padded single-line list containing
            # integers, reals and quoted strings.  Perfect for using csv.reader to parse...  Not
            # quite perfect: doesn't handle trailing whitespace after quoted strings quite right,
            # but much better than we can do by hand.
            try:
                val_list,	= csv.reader(
                    [ val ], quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True )
            except Exception as exc:
                log.normal( "Invalid sequence of CSV values: %s; %s", val, exc )
                raise
            opr['data']		= list( map( cast, val_list ))

            if 'offset' not in opr and not fragment:
                # Non-fragment write.  The exact correct number of data elements must be
                # provided. If not specified, deduce it.
                if 'elements' not in opr:
                    opr['elements'] = len( opr['data'] )
                assert len( opr['data'] ) == opr['elements'], \
                    "Number of data values (%d: %r) doesn't match element count (%d): %s=%s" % (
                        len( opr['data'] ), opr['data'], opr['elements'], tag, val )
            else:
                # Known element size; allow Fragmented write, to an identified range of indices optionally w/offset into a
                # buffer of known type, hence we can check length.  If the byte offset + data
                # provided doesn't match the number of elements, then a subsequent Write Tag
                # Fragmented command will be required to write the balance.  We can't deduce the
                # final total number of elements from the data provided, b/c it may be partial.
                assert size and 'elements' in opr, \
                    "Fragmented write must specify exact size and destination element range"
                byte		= opr.get( 'offset' ) or 0
                assert byte % size == 0, \
                    "Invalid byte offset %d for elements of size %d bytes" % ( byte, size )
                beg		= byte // size
                end		= beg + len( opr['data'] )
                assert end <= opr['elements'], \
                    "Number of elements (%d) provided and byte offset %d / %d-byte elements exceeds element count %d: %r" % (
                        len( opr['data'] ), byte, size, opr['elements'], opr )
                if beg != 0 or end != opr['elements']:
                    log.detail( "Partial Write Tag Fragmented; elements %d-%d of %d", beg, end-1, opr['elements'] )

        if kwds:
            log.detail("Tag: %r yields Operation: %r.update(%r)", tag, opr, kwds )
            opr.update( kwds )
        else:
            log.detail("Tag: %r yields Operation: %r", tag, opr )
        yield opr


def enip_replies( response, multiple=False ):
    """Return valid EtherNet/IP response(s), or Falsey (None if nothing, {} if EOF).  Raises Exception
    if invalid response, EnipStatusError if valid but unsuccessful.

    Find the replie(s) in the response; could be single or multiple; should match requests!
    Unfortuantely, it is *impossible* to determine this without *knowing* if the issued request was
    a Multiple Service Packet; at a higher level (where we collect responses for each issued
    request), we can determine if the service code matches.

    Returns a list of replies on success.

    """
    if response is None:	# None response indicates timeout
        return None		# "Response Not Received w/in timeout
    elif not response:		# empty response indicates clean EOF
        return response 	# "Session terminated" # =~= raise StopIteration( "Session terminated" )
    elif 'enip.status' not in response:
        raise AssertionError( "Failed to receive EtherNet/IP response: %s", parser.enip_format( response ))
    elif response.enip.status != 0:
        raise ENIPStatusError( status=response.enip.status )
    replies			= None
    item_1			= response.get( 'enip.CIP.send_data.CPF.item[1]' )
    if item_1:
        # Could be either Send RR Data or Send Unit Data
        data			= item_1.get( 'unconnected_send' ) or item_1.get( 'connection_data' )
        if data:
            # Could be a Multiple Service Packet or a single Service request.  Multiple
            # Service Packet is eg. a list of read/write_tag/frag; Single request is eg. a
            # read/write_tag/frag, converted to a list.
            request		= data.get( 'request' )
            if 'multiple.request' in request:
                replies		= request.multiple.request
            else:
                replies		= [ request ]
    assert replies, \
        "Response Unrecognized: %s" % ( parser.enip_format( response ))
    return replies


class client( object ):
    """Establish a connection (within timeout), and Transmit request(s), and yield replies as
    available.  The request will fail (raise exception) if it cannot be sent within the specified
    timeout (None, if no timeout desired).  After a session is registered, transactions may be
    pipelined (requests sent before responses to previous requests are received.)

    Issue requests immediately (avoid delays due to Nagle's Algorithm) to effectively maximize
    thruput on high-latency links.  Also enable keep-alive on the socket, to be able to (eventually)
    detect half-open sockets (depends on the kernel's TCP/IP keepalive timer settings.)

    Provide an alternative enip.device.Message_Router Object class instead of the (default) Logix,
    to parse alternative sub-dialects of EtherNet/IP.


    The first client created also sets the global "device.dialect"; all connections must use the
    same dialect.  The default is Logix.

    """
    route_path_default		= defaults.route_path_default
    send_path_default		= defaults.send_path_default
    priority_time_tick		= defaults.priority_time_tick
    timeout_ticks		= defaults.timeout_ticks

    def __init__( self, host, port=None, timeout=None, dialect=None, profiler=None,
                  udp=False, broadcast=False, source_address=None, configuration=None ):
        """Connect to the EtherNet/IP client, waiting up to 'timeout' for a connection.  Avoid using
        the host OS platform default if 'host' is empty; this will be different on Mac OS-X, Linux,
        Windows, ...  So, for an empty host, we'll default to 'localhost'; this should be IPv4/IPv6
        compatible (vs. '127.0.0.1', for example).  Likewise, if both the supplied port and
        defaults.address ends up 0, the OS-supplied default port is not used; use 44818.

        If 'udp' specified and a 'broadcast' is intended, then we won't connect the UDP socket
        (allowing multiple peers, and we'll set OS_BROADCAST.

        It is not recommended to use 'broadcast' when high reliability is required.  Since all
        responses are parsed one after another by the same EtherNet/IP CIP response parser, an
        invalid CIP response will cause the parser to fail.  Instead, issue a broadcast "List
        Services/Identity/Interfaces" request, and then manually collect the peer replies and
        addresses using recvfrom.  Then, issue individual requests to each identified peer.

        If source_address "<address>[:<port>]" is specified, we'll attempt to bind to that
        interface, and send using the specified source address (and optionally port number).

        If host of None is provided, we'll load the default from 'Address' in the named
        'configuration' section.

        """
        # Bind to nothing by default (use default i'face as source address).  Otherwise, use the
        # specified interface (or the system default, specified by ''), and the specified port (or
        # an ephemeral port, specified by 0).
        self.ifce		= None
        if source_address:
            ifce		= source_address.split( ':', 1 )
            self.ifce		= ( str( ifce[0] ), int( ifce[1] if len( ifce ) > 1 else 0 ))

        # If no 'host' supplied; get from 'Address' in configuration.  Default is 
        if host is None:
            addr_str		= device.Object.config_override( host, 'Address', default='', section=configuration ).strip()
            host,port_cnf	= misc.parse_ip_port( addr_str, default=('localhost',defaults.address[1]) )
            if port is None:
                port	= port_cnf # only override if nonexistent/None
        if port is None:
            port		= defaults.address[1]
        self.addr		= str( host ),int( port ) # host may be ip_address; str-ingify...
        self.addr_connected	= not ( udp and broadcast )
        self.conn		= None
        self.udp		= udp
        self.dialect		= dialect # May be (temporarily) changed
        # If provided, we'll disable/enable a profiler around the I/O code, to avoid corrupting the
        # profile data with arbitrary I/O related delays
        self.profiler		= profiler

        log.detail( "Connect:  %s/IP to %r%s%s", "UPD" if udp else "TCP", self.addr,
                    " via %r" % ( self.ifce, ) if self.ifce else "",
                    " broadcast" if not self.addr_connected else "" )
        if self.udp:
            try:
                self.conn		= socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
                if self.ifce:
                    self.conn.bind( self.ifce )
                if not broadcast:
                    self.conn.connect( self.addr )
            except Exception as exc:
                log.normal( "Couldn't %s to EtherNet/IP UDP server at %s:%s%s: %s",
                            "broadcast" if broadcast else "connect",
                            self.addr[0], self.addr[1],
                            ( " via interface %s:%d" % ( self.ifce[0], self.ifce[1] )) if self.ifce else "",
                            exc )
                raise
            if broadcast:
                try:
                    self.conn.setsockopt( socket.SOL_SOCKET, socket.SO_BROADCAST, 1 )
                except Exception as exc:
                    log.warning( "Couldn't set SO_BROADCAST on socket to EtherNet/IP server at %s:%s: %s",
                                 self.addr[0], self.addr[1], exc )
        else:
            try:
                # If interface specified, use it.  Maintain pre-2.7 socket.create_connection
                # compatibility by avoiding the argument unless specified...
                if self.ifce:
                    self.conn		= socket.create_connection( self.addr, timeout=timeout,
                                                                    source_address=self.ifce )
                else:
                    self.conn		= socket.create_connection( self.addr, timeout=timeout )
            except Exception as exc:
                log.normal( "Couldn't connect to EtherNet/IP TCP server at %s:%s%s: %s",
                            self.addr[0], self.addr[1],
                            ( " via interface %s:%d" % ( self.ifce[0], self.ifce[1] )) if self.ifce else "",
                            exc )
                raise
            try:
                self.conn.setsockopt( socket.IPPROTO_TCP, socket.TCP_NODELAY, 1 )
            except Exception as exc:
                log.warning( "Couldn't set TCP_NODELAY on socket to EtherNet/IP server at %s:%s: %s",
                             self.addr[0], self.addr[1], exc )
            try:
                self.conn.setsockopt( socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1 )
            except Exception as exc:
                log.warning( "Couldn't set SO_KEEPALIVE on socket to EtherNet/IP server at %s:%s: %s",
                             self.addr[0], self.addr[1], exc )

        self.session		= None	# Not set w/in client class; set manually, or in derived class
        self.source		= chainable()
        self.data		= None
        # Parsers
        self.engine		= None # EtherNet/IP frame parsing in progress
        self.frame		= parser.enip_machine( terminal=True )
        self.cip		= parser.CIP( terminal=True )	# Parses a CIP   request in an EtherNet/IP frame

        # Ensure the requested dialect matches the globally selected dialect; Default to Logix. An
        # EtherNet/IP CIP "server" receives requests containing a .path identifying the target
        # Object (and its parser). The client doesn't have this when parsing responses; only when
        # producing requests. Since the responses are parsed asynchronously and then matched up with
        # the corresponding request alter (for pipelining), we need to remember a default
        # parser. Normally, this will be a Message Router derived class (eg. logix.Logix). However,
        # for some requests (eg. Forward Open), the target is the Connection Manager; we'll
        # (temporarily) change the client.dialect while parsing these requests.
        if device.dialect is None:
            from . import logix # Avoid recursive module load
            device.dialect	= logix.Logix if dialect is None else dialect
        if dialect is not None:
            assert device.dialect is dialect, \
                "Inconsistent EtherNet/IP dialect requested: %r (vs. default: %r)" % ( dialect, device.dialect )

    def __str__( self ):
        return "%s:%s[%r]" % ( self.addr[0], self.addr[1], self.session )

    def __repr__( self ):
        return "<%s %s>" % ( self.__class__.__name__, self )

    def shutdown( self ):
        """A client-initiated clean shutdown of the EtherNet/IP session requires the client to close the
        outgoing half of its TCP/IP connection, while harvesting the remaining responses incoming.
        The peer will receive EOF, and cleanly close the connection.  After the final response is
        harvested, we will then receive EOF, and close the connection.  All TCP/IP buffers will be
        clear, and the connection will then close in a completely clean fashion.

        """
        if not self.udp:
            try:
                self.conn.shutdown( socket.SHUT_WR )
            except:
                pass

    def close( self ):
        """The lifespan of an EtherNet/IP CIP client connection is defined by client.__init__() and client.close()"""
        if getattr( self, 'conn', None ) is not None:
            self.conn.close()
            self.conn	= None

    def __del__( self ):
        """Avoid invoking superclass .close, if we've already completed closing"""
        if getattr( self, 'conn', None ) is not None:
            self.close()

    def __enter__( self ):
        self.frame.__enter__()
        return self

    def __exit__( self, typ, val, tbk ):
        """We are leaving exclusive access to this client w/o having raised an Exception; we
        better be "between" frames!  If we have a partially parsed EtherNet/IP frame in
        progress, then this client is no longer usable; raise an Exception."""
        self.frame.__exit__( typ, val, tbk )
        if typ is None:
            assert self.engine is None, \
                "Partial response parsed; client session is no longer valid: %s" % ( self.engine )

    def __iter__( self ):
        return self

    def __next__( self ):
        """Return the next available response, or None if no complete response is available w/o
        blocking.  Raises StopIteration (cease iterating) on EOF between frames.  Any other
        Exception indicates a client failure, and should result in the client instance being
        discarded.
        
        If no input is presently available, harvest any input immediately available; terminate on
        EOF.

        The response may not actually contain a payload, eg. if the EtherNet/IP header contains a
        non-zero status.

        TODO: Defer parsing of CPF items in response payload to caller; only the caller knows the
        corresponding request, and hence the correct CIP Object that knows how to parse the
        request's reply! For example, a "Forward Open" is known to the Connection_Manager @6/1,
        while most I/O requests (eg. "Get Attribute Single", "Read Tag Fragmented") are known to the
        device-specific dialect of Message Router (eg. Logix). The request has the .path component
        that identifies this Object...

        """
        # Ensure that the caller has gained exclusive access to this client instance using:
        # 
        #     with <instance>:
        # 
        # So long as the caller retains exclusive access, they may continue to attempt to parse
        # a response.  They may *only* safely release exclusive access between fully parsed
        # EtherNet/IP frames (checked in __exit__, above)
        self.frame.safe()

        # Harvest any input immediately available, if we're empty.  We may be coming back
        # here after already having issued a non-transition event from the existing EtherNet/IP
        # framer engine -- we can't re-enter the engine w/o getting some more input.
        addr			= self.addr # TCP/IP; may continue parsing data rx last time thru
        if self.source.peek() is None:
            if self.profiler:
                self.profiler.disable()
            try:
                rcvd,addr	= self.recvfrom( timeout=0 )
                log.info(
                    "EtherNet/IP<--%16s:%-5s rcvd %5d: %r",
                    addr[0] if addr else None, addr[1] if addr else None,
                    len( rcvd ) if rcvd is not None else 0, rcvd )
                if rcvd is not None:
                    # Some input (or EOF); source is empty; chain the input and drop back into 
                    # the framer engine.  It will detect a no-progress condition on EOF.  If we
                    # don't have an engine, we can signal completion right here.
                    if len( rcvd ):
                        self.source.chain( rcvd )	# More input received
                    else:
                        logging.info( "EOF w/ %s input available, engine %s",
                                      "empty" if self.source.peek() is None else " some",
                                      "off" if self.engine is None else "running" )
                        if self.engine is None:
                            raise StopIteration		# EOF between EtherNet/IP frames; Done.
                else:
                    # Don't create parsing engine 'til we have some I/O to process.  This avoids the
                    # degenerate situation where empty I/O (EOF) always matches the empty command (used
                    # to indicate the end of an EtherNet/IP session).
                    if self.engine is None:
                        return None
            finally:
                if self.profiler:
                    self.profiler.enable()

        # Initiate or continue parsing input using the machine's engine; discard the engine at
        # termination or on error (Exception).  Any exception (including cpppo.NonTerminal) will be
        # propagated.  Identifies the responding peer address, by returning it via 'result.peer'.
        result			= None
        try:
            if self.engine is None:
                self.data	= dotdict( peer=addr )
                self.engine	= self.frame.run( source=self.source, data=self.data )
                
            for mch,sta in self.engine:
                if sta is None and self.source.peek() is None:
                    # Non-transition, and no input available; go get some -- all blocking is done
                    # externally (in the caller), to allow full operation on I/O latency.  On a
                    # non-transition from a sub-machine, just loop if input is still available.
                    return None
            # Engine has terminated w/ a recognized EtherNet/IP frame.
        except Exception as exc:
            log.normal( "EtherNet/IP<x>%16s:%-5d err.: %s",
                         self.addr[0], self.addr[1], str( exc ))
            self.engine		= None
            raise

        if self.frame.terminal:
            log.info( "EtherNet/IP   %16s:%-5d done: %s -> %10.10s; next byte %3d: %-10.10r: %r",
                        self.addr[0], self.addr[1], self.frame.name_centered(), self.frame.current, 
                        self.source.sent, self.source.peek(), self.data )
            # Got an EtherNet/IP frame.  Return it (after parsing its payload.)
            self.engine		= None
            result		= self.data

        # Parse the EtherNet/IP encapsulated CIP frame, if any.  If the EtherNet/IP header .size was
        # zero, it's status probably indicates why.
        if result is not None and 'enip.input' in result:
            with self.cip as machine:
                with contextlib.closing( machine.run(
                        path='enip', source=peekable( result.enip.input ), data=result )) as engine:
                    for m,s in engine:
                        pass
                assert machine.terminal, "No CIP payload in the EtherNet/IP frame: %r" % ( result )

        # Parse the device (eg. Logix) request responses in the EtherNet/IP CIP payload's CPF items
        if result is not None and 'enip.CIP.send_data' in result:
            request		= None
            for item in result.enip.CIP.send_data.CPF.item:
                if 'unconnected_send.request' in item:
                    request	= item.unconnected_send.request
                elif 'connection_data.request' in item:
                    request	= item.connection_data.request
                else:
                    continue
                assert request and 'input' in request, \
                    "Response did not contain a recognized CIP send_data CPF item"
                # A Connected/Unconnected Send that contained an encapsulated request (ie. not just a Get
                # Attribute All).  Use the globally-defined cpppo.server.enip.client's dialect's
                # (eg. logix.Logix) parser to parse the contents of the CIP payload's CPF items.
                dialect	= self.dialect or device.dialect # May be (temporarily) changed
                with dialect.parser as machine:
                    with contextlib.closing( machine.run( # for pypy, where gc may delay destruction of generators
                            source=peekable( request.input ),
                            data=request )) as engine:
                        for m,s in engine:
                            pass
                        assert machine.terminal, "No %r request in the EtherNet/IP CIP CPF frame: %r" % (
                            dialect, result )
            if log.isEnabledFor( logging.DETAIL ):
                log.detail( "Client CIP Rcvd: %s", parser.enip_format(
                    result if log.isEnabledFor( logging.INFO ) else result.enip.CIP ))
        return result

    next = __next__ # Python 2/3 compatibility

    def recvfrom( self, timeout=None ):
        """Receive data (if any) and source address, if available within timeout."""
        addr			= self.addr
        if self.addr_connected:
            rcvd		= network.recv( self.conn, timeout=timeout )
        else:
            rcvd,addr		= network.recvfrom( self.conn, timeout=timeout )
        return rcvd,addr

    def send( self, request, timeout=None ):
        """Send encoded request data."""
        assert self.writable( timeout=timeout ), \
            "Failed to send to %r within %7.3fs: %r" % (
                self.addr, misc.inf if timeout is None else timeout, request )
        sent			= bytes( request )
        if self.addr_connected:
            self.conn.sendall( sent ) # ensure full buffer is sent
        else:
            self.conn.sendto( sent, self.addr )
        log.info(
            "EtherNet/IP-->%16s:%-5d send %5d: %r",
                    self.addr[0], self.addr[1], len( request ), sent )

    def writable( self, timeout=None ):
        if self.profiler:
            self.profiler.disable()
        try:
            r, w, e		= select.select( [], [self.conn.fileno()], [], timeout )
        finally:
            if self.profiler:
                self.profiler.enable()
        return len( w ) > 0

    def readable( self, timeout=None ):
        if self.profiler:
            self.profiler.disable()
        try:
            r, w, e		= select.select( [self.conn.fileno()], [], [], timeout )
        finally:
            if self.profiler:
                self.profiler.enable()
        return len( r ) > 0

    # Basic CIP Requests; sent immediately
    def register( self, timeout=None, sender_context=b'' ):
        cip			= dotdict()
        cip.register		= {}
        cip.register.options 	= 0
        cip.register.protocol_version = 1
        return self.cip_send( cip=cip, sender_context=sender_context, timeout=timeout )

    def list_interfaces( self, timeout=None, sender_context=b'' ):
        cip			= dotdict()
        cip.list_interfaces	= {}
        return self.cip_send( cip=cip, sender_context=sender_context, timeout=timeout )

    def list_services( self, timeout=None, sender_context=b'' ):
        cip			= dotdict()
        cip.list_services	= {}
        return self.cip_send( cip=cip, sender_context=sender_context, timeout=timeout )

    def list_identity( self, timeout=None, sender_context=b'' ):
        cip			= dotdict()
        cip.list_identity	= {}
        return self.cip_send( cip=cip, sender_context=sender_context, timeout=timeout )

    def legacy( self, command, cip=None, timeout=None, sender_context=b'' ):
        """Transmit a Legacy EtherNet/IP CIP request, using the specified command code (eg. 0x0001).
        If CIP is None, then no CIP payload will be generated.

        """
        return self.cip_send( cip=cip )

    # CIP Send...Data Requests; may be deferred (eg. for Multiple Service Packet)
    def forward_open( self, path, connection_path,
                      priority_time_tick, timeout_ticks,
                      O_T, T_O, O_serial, O_vendor, connection_serial,
                      transport_class_triggers, connection_timeout_multiplier,
                      timeout=None, send=True,
                      route_path=False, send_path='', sender_context=b'',
                      **kwds ):
        """Forward Open uses a CPF encapsulation, but with no route_path or send_path.  Must be used
        with a self.dialect == Connection_Manager to properly produce request and parse response.

        """
        req			= dotdict()
        req.path		= { 'segment': [
            dotdict( d )
            for d in device.parse_path( path )
        ]}
        req.forward_open 	= {}
        fo			= req.forward_open
        fo.priority_time_tick	= priority_time_tick
        fo.timeout_ticks	= timeout_ticks
        fo.O_T			= defaults.Connection( **( O_T or {} )).decoding
        fo.T_O			= defaults.Connection( **( T_O or {} )).decoding
        fo.connection_serial	= connection_serial
        fo.O_vendor		= O_vendor
        fo.O_serial		= O_serial
        fo.transport_class_triggers = transport_class_triggers
        fo.connection_timeout_multiplier = connection_timeout_multiplier
        fo.connection_path	= { 'segment': [
            dotdict( d ) for d in device.parse_connection_path( connection_path )
        ]}
        if send:
            self.unconnected_send(
                request=req, route_path=route_path, send_path=send_path, timeout=timeout,
                sender_context=sender_context )
        return req

    def forward_close( self, path, connection_path,
                       priority_time_tick, timeout_ticks,
                       O_serial, O_vendor, connection_serial,
                       timeout=None, send=True,
                       route_path=False, send_path='', sender_context=b'' ):
        req			= dotdict()
        req.path		= { 'segment': [
            dotdict( d ) for d in device.parse_path( path )
        ]}
        req.forward_close 	= {}
        fc			= req.forward_close
        fc.priority_time_tick	= priority_time_tick
        fc.timeout_ticks	= timeout_ticks
        fc.connection_serial	= connection_serial
        fc.O_vendor		= O_vendor
        fc.O_serial		= O_serial
        fc.connection_path	= { 'segment': [
            dotdict( d ) for d in device.parse_connection_path( connection_path )
        ]}
        if send:
            self.unconnected_send(
                request=req, route_path=route_path, send_path=send_path, timeout=timeout,
                sender_context=sender_context )
        return req

    def service_code( self, code, path, data=None, elements=None, tag_type=None,
                      route_path=None, send_path=None, timeout=None, send=True,
                      data_size=None, # for response data_size estimation
                      sender_context=b'', **kwds ):
        """Generic CIP Service Code, with path to target CIP Object, and supplied data payload (converted
        to USINTs, if necessary).  Minimally, we require the service, and an indication that it is a
        bare Service Code request w/ no data:

            data.service = 0x??
            data.service_code = True

        if a data payload is required, supply 'data' (and optionally a tag_type), and this will produce:

            data.service = 0x??
            data.service_code.data = [0, 1, 2, 3]

        """
        req			= dotdict()
        req.path		= { 'segment': [
            dotdict( d ) for d in device.parse_path( path )
        ]}
        req.service		= code
        if data is None:
            req.service_code	= True		# indicate a payload-free Service Code request
        else:
            # If a tag_type has been specified, then we need to convert the data to SINT/USINT.
            if elements is None:
                elements	= len( data )
            else:
                assert elements == len( data ), \
                    "Inconsistent elements: %d doesn't match data length: %d" % ( elements, len( data ))
            if tag_type not in (None,parser.SINT.tag_type,parser.USINT.tag_type):
                usints		= [ v for v in bytearray(
                    parser.typed_data.produce( data={'tag_type': tag_type, 'data': data } )) ]
                log.detail( "Converted %s[%d] to USINT[%d]",
                            parser.typed_data.TYPES_SUPPORTED[tag_type], elements, len( usints ))
                data,elements	= usints,len( usints )
            req.service_code	= {}
            req.service_code.data = data

        # We always render the transmitted data payload for Service Code
        req.input		= bytearray()
        if data is not None:
            req.data		= data
            req.input	       += bytearray( parser.typed_data.produce( req, tag_type=parser.USINT.tag_type ))
        if send:
            self.req_send(
                request=req, route_path=route_path, send_path=send_path, timeout=timeout,
                sender_context=sender_context, **kwds )
        return req

    def get_attributes_all( self, path,
              route_path=None, send_path=None, timeout=None, send=True,
              data_size=None, elements=None, tag_type=None, # for response data_size estimation
              sender_context=b'', **kwds ):
        req			= dotdict()
        req.path		= { 'segment': [
            dotdict( d ) for d in device.parse_path( path )
        ]}
        req.get_attributes_all	= True
        if send:
            self.req_send(
                request=req, route_path=route_path, send_path=send_path, timeout=timeout,
                sender_context=sender_context, **kwds )
        return req

    def get_attribute_single( self, path,
              route_path=None, send_path=None, timeout=None, send=True,
              data_size=None, elements=None, tag_type=None, # for response data_size estimation
              sender_context=b'', **kwds ):
        req			= dotdict()
        req.path		= { 'segment': [
            dotdict( d ) for d in device.parse_path( path )
        ]}
        req.get_attribute_single= True
        if send:
            self.req_send(
                request=req, route_path=route_path, send_path=send_path, timeout=timeout,
                sender_context=sender_context, **kwds )
        return req

    def set_attribute_single( self, path, data, elements=1, tag_type=None,
              route_path=None, send_path=None, timeout=None, send=True,
              sender_context=b'', **kwds ):
        """Convert the supplied tag_type data into USINTs if necessary, and perform the Set Attribute
        Single.  If no/None tag_type supplied, the data is assumed to be SINT/USINT.

        """
        # If a tag_type has been specified, then we need to convert the data to SINT/USINT.
        if elements is None:
            elements		= len( data )
        else:
            assert elements == len( data ), \
                "Inconsistent elements: %d doesn't match data length: %d" % ( elements, len( data ))
        if tag_type not in (None,parser.SINT.tag_type,parser.USINT.tag_type):
            usints		= [ v for v in bytearray(
                parser.typed_data.produce( data={'tag_type': tag_type, 'data': data } )) ]
            log.detail( "Converted %s[%d] to USINT[%d]",
                        parser.typed_data.TYPES_SUPPORTED[tag_type], elements, len( usints ))
            data,elements	= usints,len( usints )
        req			= dotdict()
        req.path		= { 'segment': [
            dotdict( d ) for d in device.parse_path( path )
        ]}
        req.set_attribute_single= {
            'data':		data,
            'elements':		elements,
        }
        if send:
            self.req_send(
                request=req, route_path=route_path, send_path=send_path, timeout=timeout,
                sender_context=sender_context, **kwds )
        return req

    def read( self, path, elements=1, offset=0,
              route_path=None, send_path=None, timeout=None, send=True,
              data_size=None, tag_type=None, # for response data_size estimation
              sender_context=b'', **kwds ):
        """Issue a Read Tag Fragmented request for the specified path.  If no specific number of
        elements is specified, get it from the path (if it is unparsed, eg Tag[0-9] or
        @0x04/5/connection=100)

        The Read Tag [Fragmented] response carries a data type; this may be a simple CIP type
        (eg. DINT == 0x00c4), or it may indicate a C*Logix STRUCT == 0x02a0 + a UINT structure_tag).

        We cannot parse these complex STRUCT types until we get the complete return value, since an
        individual Read Tag [Fragmented] may return partial data -- and probably not fill STRUCT
        records.  So, we do not bother to transmit tag_type data describing the STRUCT, as it cannot
        be used 'til the full response has been collected, possibly over several Read Tag
        [Fragmented] calls.  Thus, all STRUCT responses are returned as raw USINT data.

        """
        req			= dotdict()
        seg,elm,cnt		= device.parse_path_elements( path )
        if cnt is not None:
            elements		= cnt
        req.path		= { 'segment': [ dotdict( s ) for s in seg ]}
        if offset is None:
            req.read_tag	= {
                'elements':	elements
            }
        else:
            req.read_frag	= {
                'elements':	elements,
                'offset':	offset,
            }
        if send:
            self.req_send(
                request=req, route_path=route_path, send_path=send_path, timeout=timeout,
                sender_context=sender_context, **kwds )
        return req

    def write( self, path, data, elements=1, offset=0, tag_type=None,
               route_path=None, send_path=None, timeout=None, send=True,
               sender_context=b'', **kwds ):
        req			= dotdict()
        seg,elm,cnt		= device.parse_path_elements( path )
        if cnt is not None:
            elements		= cnt
        req.path		= { 'segment': [ dotdict( s ) for s in seg ]}
        if tag_type is None:
            tag_type		= parser.INT.tag_type
        if offset is None:
            req.write_tag	= {
                'elements':	elements,
                'data':		data,
                'type':		tag_type,
            }
        else:
            req.write_frag	= {
                'elements':	elements,
                'offset':	offset,
                'data':		data,
                'type':		tag_type,
            }
        if send:
            self.req_send(
                request=req, route_path=route_path, send_path=send_path, timeout=timeout,
                sender_context=sender_context, **kwds )
        return req

    def multiple( self, request, path=None, route_path=None, send_path=None, timeout=None, send=True,
                  sender_context=b'', **kwds ):
        assert isinstance( request, list ), \
            "A Multiple Service Packet requires a request list"
        req			= dotdict()
        if path:
            req.path		= { 'segment': [
                dotdict( s ) for s in device.parse_path( path )
            ]}
        req.multiple		= {
            'request':		request,
        }
        if send:
            self.req_send(
                request=req, route_path=route_path, send_path=send_path, timeout=timeout,
                sender_context=sender_context, **kwds )
        return req

    # 
    # ..._send -- transmit a request using the appropriate encapsulation
    # 
    #     Depending on the class of CIP connection, various encapsulations are appropriate.  These
    # should be as close to transparent to the higher-level APIs as possible; for consistency, we'll
    # accept all of the required arguments, ignoring any that are irrelevant (in case they are
    # provided in general-purpose higher-level code).
    # 
    def unconnected_send( self, request, route_path=None, send_path=None, timeout=None,
                          connection=None, sequence=None, # ignored
                          priority_time_tick=None, timeout_ticks=None,
                          sender_context=b'', dialect=None ):
        """The default route_path is the CPU in chassis (link 0), port 1, and the default send_path is
        to its Connection Manager (Class 6, Instance 1).  These defaults can be configured on a
        class or per-instance basis by changing the {route,send}_path_default attributes in either
        the client class or instance.

        If a specific dialect of CIP Object is required to parse/produce the message, pass it;
        otherwise, the global device.dialect will be used. For example; only Connection_Manager type
        Objects can understand Forward Open/Close requests. Otherwise, it is probably a
        Message_Router type CIP Object that is required to parse the payload.

        """
        # Default route_path to the CPU in chassis (link 0), port 1.  If provided route_path is
        # 0/False, then disable (no route_path provided to Unconnected Send)
        if route_path is None:
            route_path		= self.route_path_default
        if route_path:
            route_path		= device.parse_route_path( route_path )
            assert send_path or send_path is None, \
                "Must supply a send_path (or None for default), if route_path supplied"
        if send_path is None: # could be a string path to parse or a list
            send_path		= self.send_path_default # Default to the Connection Manager
        if send_path:
            send_path		= device.parse_path( send_path )
        if dialect is None:
            dialect		= self.dialect or device.dialect # May be (temporarily) changed

        cip			= dotdict()
        cip.send_data		= {}

        sd			= cip.send_data
        sd.interface		= 0
        sd.timeout		= 8 # 0 # was 0; unknown functionality...
        sd.CPF			= {}
        sd.CPF.item		= [ dotdict(), dotdict() ]
        sd.CPF.item[0].type_id	= 0x00 # 0
        sd.CPF.item[1].type_id	= 0xb2 # 178
        sd.CPF.item[1].unconnected_send = {}

        # If a non-empty send_path or route_path is desired, we'll need to use a Logix-style service
        # 0x52 Unconnected Send within the SendRRData to carry these details.  Only Originating
        # Devices and devices that route between links need to implement this.  Otherwise, for
        # simple non-routing CIP devices (eg. MicroLogix, AB PowerFlex, ...) just go straight to the
        # command payload.
        us			= sd.CPF.item[1].unconnected_send
        if send_path or route_path:
            us.service		= 0x52 # == 82
            us.status		= 0
            us.priority		= self.priority_time_tick if priority_time_tick is None else priority_time_tick
            us.timeout_ticks	= self.timeout_ticks      if timeout_ticks      is None else timeout_ticks
            us.path		= { 'segment': [
                dotdict( s ) for s in send_path
            ]}
            if route_path: # May be None/0/False or empty, to eliminate routing encapsulation
                us.route_path	= { 'segment': [
                    dotdict( s ) for s in route_path
                ]}

        # If the paylaod is an opaque byte string, just pass it thru (we probably don't know how to
        # en/decode it, eg. raw PCCC requests, etc.).  However, if dict is provided, we'll try (the
        # usual case).
        if isinstance( request, dict ):
            # Normally, the request will be a dotdict containing the broken-out details of a CIP request
            # (eg. something containing a CIP '.service' number or request details like
            # '.get_attribute_single', '.read_tag', etc.).  However, there are times when we might just
            # be transporting or forwarding an opaque (unparsed) request destined for some other object.
            # If a device.RequestUnrecognized exception occurs, then check if there's already a
            # request.input; if so, use it.
            us.request		= request
            try:
                us.request.input= bytearray( dialect.produce( us.request )) # eg. logix.Logix
            except device.RequestUnrecognized:
                if 'input' not in us.request:
                    raise # No request, and no already-produced serialization
        else:
            us.request		= {}
            us.request.input	= bytearray( request or b'' )

        return self.cip_send( cip=cip, sender_context=sender_context, timeout=timeout )

    def connected_send( self, request, timeout=None,
                        connection=None, sequence=None,
                        priority_time_tick=None, timeout_ticks=None, # ignored
                        sender_context=b'', dialect=None ):
        """A connected send is much like an unconnected_send, except its CPF contains a 0x00a1
        connection ID, and a 0x00b1 data sequence number and payload.  Defaults to 0 connection ID,
        0 sequence number; the caller should increment sequence between calls.

        If payload is a dict, we'll try to produce it; otherwise, assumes request is an opaque byte
        string.

        Uses dialect, self.dialect or device.dialect (in that order).

        """
        # The payload may be an opaque byte string; we probably don't know how to en/decode it.
        # However, if dict is provided, we'll try.
        if dialect is None:
            dialect		= self.dialect or device.dialect

        cip			= dotdict()
        cip.send_data		= {}

        sd			= cip.send_data
        sd.interface		= 0
        sd.timeout		= 8 # 0 # was 0; unknown functionality...
        sd.CPF			= {}
        sd.CPF.item		= [ dotdict(), dotdict() ]
        sd.CPF.item[0].type_id	= 0xa1 # 161
        sd.CPF.item[0].connection_ID = {}
        sd.CPF.item[0].connection_ID.connection = connection or 0
        sd.CPF.item[1].type_id	= 0xb1 # 177
        sd.CPF.item[1].connection_data = {}

        cd			= sd.CPF.item[1].connection_data
        cd.sequence		= sequence or 0

        if isinstance( request, dict ):
            cd.request		= request
            try:
                cd.request.input= bytearray( dialect.produce( request ))
            except device.RequestUnrecognized:
                if 'input' not in cd.request:
                    raise # No request, and no already-produced serialization
        else:
            cd.request		= {}
            cd.request.input	= bytearray( request or b'' )

        # Use EtherNet/IP command 0x0070 SendUnitData, instead of (default) 0x006f SendRRData
        return self.cip_send( cip=cip, command=0x0070, sender_context=sender_context, timeout=timeout )

    def cip_send( self, cip, command=None, timeout=None, sender_context=b'' ):
        """Encapsulates the CIP request and transmits it, returning the full encapsulation structure
        used to carry the request.  The response must be harvested later; a sender_context should be
        supplied that may be used to associate the response to the originating request.

        WARNING: Astonishingly, C*Logix PLCs do *not* include the supplied Sender Context in the
        response for requests carried on an "Implicit" connection!  So, you *must* use the default
        b'' for all requests on an Implicit connection.

        If the CIP contents can be used to deduce the correct EtherNet/IP CIP framing command
        (eg. contains a recognized payload, such as ...CIP.list_identity or ...CIP.send_data), then
        command may remain None.  However, if sending "legacy" CIP requests (eg. 0x0001) with no CIP
        payload, then command may be used to specify the data.enip.command for EtherNet/IP framing.

        """
        data			= dotdict()
        data.enip		= {}
        if command:
            data.enip.command	= command
        data.enip.session_handle= self.session or 0 # May be None, if not yet registered
        data.enip.options	= 0
        data.enip.status	= 0
        data.enip.sender_context= {}
        data.enip.sender_context.input = format_context( sender_context )

        data.enip.CIP		= cip		# Must have content encoded already produced

        if log.isEnabledFor( logging.DETAIL ):
            log.detail( "Client CIP Send: %s", parser.enip_format(
                data if log.isEnabledFor( logging.INFO ) else cip ))

        data.enip.input		= bytearray( parser.CIP.produce( data.enip )) # May deduce enip.command...
        data.input		= bytearray( parser.enip_encode( data.enip )) #   for EtherNet/IP framing

        log.debug( "EtherNet/IP: %3d + CIP: %3d == %3d bytes total",
                  len( data.input ) - len( data.enip.input ),
                  len( data.enip.input ), len( data.input ))

        if self.profiler:
            self.profiler.disable()
        try:
            self.send( data.input, timeout=timeout )
        finally:
            if self.profiler:
                self.profiler.enable()
        return data

    def req_send( self, request, **kwds ):
        """Sending a request on a client connector/implicit connection requires the use of the
        appropriate encapsulation.  An explicit "Unconnected" session connection normally uses a
        unconnected_send "Send RR Data".  We many have a non-default priority_time_tick or
        timeout_ticks.

        """
        return self.unconnected_send( request, **kwds )


def await_response( cli, timeout=None ):
    """Await a response on an iterable client() instance (for timeout seconds, or forever if None).
    Returns (response,elapsed).  A 'timeout' may be supplied, of:

        0         --> Immediate timeout (response must be ready)
        None      --> No timeout (wait forever for response)
        float/int --> The specified number of seconds

    Assumes that the supplied iterable (a client instance) yields None on failure to parse a frame
    with presently available input.  This is where we implement timeouts; wait up to 'timeout' for
    the client to become readable; if not, return the None.  Otherwise, loop back and continue
    trying to gain a response.

    An empty response {} indicates clean termination of a session (EOF received, with no input or
    existing partial response in process of parsing in the cli iterator.)

    """
    response			= dotdict() # Prepare for EOF
    begun			= misc.timer()
    for response in cli: # if StopIteration raised immediately, defaults to {} signalling completion
        if response is None:
            elapsed		= misc.timer() - begun
            if not timeout or elapsed <= timeout:
                # 0 (immediate) or None (infinite), or unsatisfied timeout; input pending?
                if cli.readable( timeout=timeout if not timeout else timeout - elapsed ):
                    response	= dotdict() # Prepare (again) for EOF
                    continue # Client I/O pending w/in timeout; see if response complete
            # No input available w'in timeout.  A partially parsed response may remain
            # in 'cli', which may be continued 'til the cli is released.
        break
    elapsed			= misc.timer() - begun
    log.info( "Awaited %7.3f/%7.3fs for response: %r",
              elapsed, misc.inf if timeout is None else timeout, response )
    return response,elapsed


class connector( client ):
    """Register a connection to an EtherNet/IP controller, storing the returned session_handle in
    self.session, ready for processing further requests.

    Raises an Exception if no valid connection can be established within the supplied timeout.

    NOTE:

    Generally doesn't make sense to "Register" using a UDP/IP connection to an EtherNet/IP CIP
    device, as it is not considered a valid request, so we don't issue it (self.session remains
    None).  We'll allow creation of a connector, as the client code may simply be using it to
    perform otherwise valid requests (eg. List Identity, ...).  However, we do not check for
    validity of requests issued over the connection.

    """
    def __init__( self, host, port=None, timeout=None, **kwds ): # possibly supply dialect, ...
        """Establish a TCP/IP connection and perform a successful CIP Register within 'timeout'.  Allow the
        full timeout for the TCP/IP connection to succeed.  CIP Register is not valid for UDP/IP
        type connections.

        """
        begun			= misc.timer()
        try:
            super( connector, self ).__init__( host=host, port=port, timeout=timeout, **kwds )
            if self.udp:
                return
            with self:
                # The register( timeout=... ) applies to the socket send only
                elapsed_req	= misc.timer() - begun
                self.register( timeout=None if timeout is None else max( 0, timeout - elapsed_req ))
                # Await the CIP response for remainder of timeout
                elapsed_req	= misc.timer() - begun
                data,elapsed_rpy= await_response( self, timeout=None if timeout is None else max( 0, timeout - elapsed_req ))

            assert data is not None, "Failed to receive any response"
            assert 'enip.status' in data, "Failed to receive EtherNet/IP response"
            assert data.enip.status == 0, "EtherNet/IP response indicates failure: %s" % data.enip.status
            assert 'enip.CIP.register' in data, "Failed to receive Register response"

            self.session	= data.enip.session_handle
        except Exception as exc:
            log.normal( "Connect:  Failure in %7.3f/%7.3fs: %s", misc.timer() - begun,
                        misc.inf if timeout is None else timeout, exc )
            raise
        else:
            log.normal( "Connect:  Success in %7.3f/%7.3fs", misc.timer() - begun,
                        misc.inf if timeout is None else timeout )

    def index_to_sender_context( self, index ):
        return str( index ).encode( 'iso-8859-1' )

    def issue( self, operations, index=0, fragment=False, multiple=0, timeout=None ):
        """Issue a sequence of I/O operations, returning the corresponding sequence of:
        (<index>,<context>,<descr>,<op>,<request>).  If a non-zero 'multiple' is provided, bundle
        requests 'til we exceed the specified multiple service packet request size limit.

        Each op is instrumented with a sender_context based on the provided 'index', indicating the
        actual EtherNet/IP CIP request it is part of.  This can be used to detect how many actual
        I/O requests are on the wire if some are merged into Multiple Service Packet requests and
        some are single requests.

        WARNING:Beware; C*Logix PLCs do *not* respond with the supplied Sender Context over Implicit
        "Connected" sessions.

        Requests are variable in size due to the path (may have long symbolic names).  Read replies
        and Write requests are variable in size due to data type and length.  Unfortunately, Reads
        don't specify the data type; this is decided by the type of the target Attribute.  So, any
        guesses on size of reply are estimates at best.  We'll assume 4-byte data for read replies,
        and 10-byte Tag names.

        Reads requests are ~22 bytes and replies ~4 bytes + data in response, Writes ~24 bytes +
        data in request and ~4 bytes in response.

        EtherNet/IP framing is ~24 bytes, CIP ~6, CPF + Unconnected Send ~24, Multiple Service
        Packet ~14.  So, a Multiple Service Packet request or reply has a wire-level overhead of
        24+6+24+14 == 68 bytes; about 14 bytes more than a normal single CIP request/reply.

        We must estimate the size of both the request and the reply, and attempt to ensure neither
        exceeds the target 'multiple' request and/or response size.  If data_size or elements and
        tag_type (undefined/None defaults to assume 4-byte types) is provided (strictly not
        necessary for read/get_attribute* calls), these will be used to calculate/estimate the
        response size.  Default assumption for Read Tag is 4-byte elements, for Get Attribute Single
        is an average [S]STRING, and for Get Attributes All is the maximum Multiple Service Packet
        size (so it isn't merged, by default)

        """
        sender_context		= self.index_to_sender_context( index )
        reqsiz = reqmin		= 68
        rpysiz = rpymin		= 68
        requests		= []	# If we're collecting for a Multiple Service Packet
        requests_paths		= {}	# Also, must collect all op route/send_paths
        for op in operations:
            op			= op.copy() # We'll be altering the dict, so make a shallow copy
            # Chunk up requests if using Multiple Service Request, otherwise send immediately.  Also
            # handle Get Attribute(s) Single/All, but don't include ...All in Multiple Service Packet.
            op['sender_context']= sender_context
            descr		= "Multi. " if multiple else "Single "
            begun		= misc.timer()
            method		= op.pop( 'method', 'write' if 'data' in op else 'read' )
            if method == 'write':
                descr	       += "Write "
                if 'offset' not in op:
                    op['offset']= 0 if fragment else None # Force Write Tag Fragmented
                req		= self.write( timeout=timeout, send=not multiple, **op )
                reqest		= 24 + parser.typed_data.datasize(
                    tag_type=op.get( 'tag_type' ) or parser.INT.tag_type, size=len( op['data'] ))
                rpyest		= 4
            elif method == 'read':
                descr	       += "Read  "
                if 'offset' not in op:
                    op['offset']= 0 if fragment else None # Force Read Tag Fragmented
                req		= self.read( timeout=timeout, send=not multiple, **op )
                reqest		= 22
                rpyest		= 4
                if op.get( 'data_size' ):
                    rpyest     += op.get( 'data_size' )
                else:
                    rpyest     += parser.typed_data.datasize(
                        tag_type=op.get( 'tag_type' ) or parser.DINT.tag_type, size=op.get( 'elements', 1 ))
            elif method == 'set_attribute_single':
                descr	       += "S_A_S "
                req		= self.set_attribute_single( timeout=timeout, send=not multiple, **op )
                reqest		= 8 + parser.typed_data.datasize(
                    tag_type=op.get( 'tag_type' ) or parser.USINT.tag_type, size=len( op['data'] ))
                rpyest		= 4
            elif method == 'get_attribute_single':
                descr	       += "G_A_S "
                req		= self.get_attribute_single( timeout=timeout, send=not multiple, **op )
                reqest		= 8
                rpyest		= 0
                if op.get( 'data_size' ):
                    rpyest     += op.get( 'data_size' )
                elif op.get( 'tag_type' ): # a non-0/None tag_type defined; use it (assumes 1 element Attribute)
                    rpyest     += parser.typed_data.datasize(
                        tag_type=op.get( 'tag_type' ) or parser.DINT.tag_type, size=op.get( 'elements', 1 ))
                else:
                    rpyest	= multiple # Completely unknown; prevent merging...
            elif method == 'get_attributes_all':
                descr	       += "G_A_A "
                req		= self.get_attributes_all( timeout=timeout, send=not multiple, **op )
                reqest		= 8
                rpyest		= 0
                if op.get( 'data_size' ):
                    rpyest     += op.get( 'data_size' )
                elif op.get( 'tag_type' ):
                    rpyest     += parser.typed_data.datasize(
                        tag_type=op.get( 'tag_type' ) or parser.DINT.tag_type, size=op.get( 'elements', 1 ))
                else:
                    rpyest	= multiple
            elif method == "service_code":
                req		= self.service_code( timeout=timeout, send=not multiple, **op )
                reqest		= 1 + len( req.input ) # We've rendered the Service Request payload
                rpyest		= 0
                if op.get( 'data_size' ): # Only explicit reply data_size is used; tag_type/element is for request
                    rpyest     += op.get( 'data_size' )
                else:
                    rpyest	= multiple
            else:
                assert False, "Unrecognized operation method %s: %r" % ( method, op )
            elapsed		= misc.timer() - begun
            descr	       += '    ' if 'offset' not in op else 'Frag' if op['offset'] is not None else 'Tag '
            if 'path' in op:
                descr	       += ' ' + format_path( op['path'], count=op.get( 'elements' ))

            if multiple:
                if (( not requests or max( reqsiz + reqest, rpysiz + rpyest ) < multiple )
                    and requests_paths.setdefault( 'route_path', op.get( 'route_path' )) == op.get( 'route_path' )
                    and requests_paths.setdefault(  'send_path', op.get(  'send_path' )) == op.get(  'send_path' )):
                    # Multiple Service Packet new or req/rpy est. size OK, and route/send_path same; keep collecting
                    reqsiz     += reqest
                    rpysiz     += rpyest
                else:
                    # Multiple Service Packet siz too full w/ this req (or paths differ); issue requests and queue it
                    begun	= misc.timer()
                    mul		= self.multiple( request=[r for d,o,r in requests], timeout=timeout,
                                                 sender_context=sender_context, **requests_paths )
                    elapsed	= misc.timer() - begun
                    if log.isEnabledFor( logging.DETAIL ):
                        log.detail( "Sent %7.3f/%7.3fs: %s (req: %d + %d or rpy: %d + %d >= %d): %s", elapsed,
                                    misc.inf if timeout is None else timeout, "Multiple Service Packet",
                                    reqsiz, reqest, rpysiz, rpyest, multiple,
                                    parser.enip_format( mul ))
                    log.detail( "Sending %2d (Context %10r)", len( requests ), sender_context )
                    for d,o,r in requests:
                        yield index,sender_context,d,o,r
                    index      += 1
                    requests	= []
                    requests_paths = {}
                    reqsiz	= reqmin
                    rpysiz	= rpymin
                # This op is consistent with developing multiple requests; queue it, remembering paths
                requests.append( (descr,op,req) )
                requests_paths.setdefault( 'route_path', op.get( 'route_path' ))
                requests_paths.setdefault(  'send_path', op.get( 'send_path' ))
                if log.isEnabledFor( logging.DETAIL ):
                    log.detail( "Que. %7.3f/%7.3fs: %s %s", 0, 0, descr, parser.enip_format( req ))
            else:
                # Single requests already issued
                if log.isEnabledFor( logging.DETAIL ):
                    log.detail( "Sent %7.3f/%7.3fs: %s %s", elapsed,
                                misc.inf if timeout is None else timeout, descr,
                                parser.enip_format( req ))
                log.detail( "Sending  1 (Context %10r)", sender_context )
                yield index,sender_context,descr,op,req
                index	       += 1

            sender_context	= self.index_to_sender_context( index )

        # No more operations!  Issue the (final) Multiple Service Packet w/ remaining requests
        if multiple and requests:
            begun		= misc.timer()
            mul			= self.multiple( request=[r for d,o,r in requests], timeout=timeout,
                                                 sender_context=sender_context, **requests_paths )
            elapsed		= misc.timer() - begun
            if log.isEnabledFor( logging.DETAIL ):
                log.detail( "Sent %7.3f/%7.3fs: %s %s", elapsed,
                            misc.inf if timeout is None else timeout, "Multiple Service Packet",
                            parser.enip_format( req ))
            log.detail( "Sending %2d (Context %10r)", len( requests ), sender_context )
            for d,o,r in requests:
                yield index,sender_context,d,o,r

    def collect( self, timeout=None ):
        """Yield collected request replies 'til timeout expires or session terminates (raising
        StopIteration), or until a GeneratorExit is raised (no more responses expected, and
        generator was discarded).  Yields a sequence of: (<context>,<reply>,<status>,<value>).

        <context> is a bytes string (any NUL padding on the right removed); All replies in a
        Multiple Service Packet response will have the same <context>.

        <reply> is the individual parsed read/write reply, regardless of whether it came back as an
        individual response, or as part of a Multiple Service Packet payload.

        <status> may be an int or a tuple (int,[int...]) if extended status codes returned.
        Remember: Success (0x00) and Partial Data (0x06) both return valid data!

        <value> will be True for writes, a non-empty array of data for reads, None if there was a
        failure with the request (will by Truthy on Success, Falsey on Failure.)

        """
        while True:
            if self.profiler:
                self.profiler.disable()
            try:
                response,elapsed= await_response( self, timeout=timeout )
            finally:
                if self.profiler:
                    self.profiler.enable()

            # Find the replies in the response; could be single or multiple; should match requests!
            replies		= enip_replies( response )
            if not replies: # [<replies>], None or {} (EOF), or Exception/ENIPStatusError On EOF or
                # timeout, cease responding; downstream could decide what to do on lack of matching
                # response for a previously submitted request; probably should terminate EtherNet/IP
                # CIP connection, b/c it is not impossible to reliably match future requests with
                # replies.
                log.detail( "Terminated with %s: %r", "timeout" if replies is None else "EOF", self )
                #yield response	#? Nope...
                # A timeout/EOF means no response collected, and none (reliably) expected: upstream
                # can determine "health" of that fact.
                return
            ctx			= parse_context( response.enip.sender_context.input )
            log.detail( "Receive %2d (Context %10r)", len( replies ), ctx )
            assert replies, \
                "Receive %2d (Context %10r): Mismatched; failed to locate replies in: %s" % (
                    len( replies ), ctx, parser.enip_format( response ))

            for reply in replies:
                val		= None
                sts		= reply.status			# sts = # or (#,[#...])
                # Success or read w/ Partial Data; val is Truthy
                if reply.status in (0x00,0x06) and 'read_frag' in reply:
                    val		= reply.read_frag.data
                elif reply.status in (0x00,0x06) and 'read_tag' in reply:
                    val		= reply.read_tag.data
                elif reply.status in (0x00,0x06) and 'get_attribute_single' in reply:
                    val		= reply.get_attribute_single.data
                elif reply.status in (0x00,0x06) and 'get_attributes_all' in reply:
                    val		= reply.get_attributes_all.data
                elif reply.status in (0x00,):
                    # eg. 'set_attribute_single', 'write_{tag,frag}', 'service_code', etc...
                    val		= True
                else:					# Failure; val is Falsey
                    if 'status_ext' in reply and reply.status_ext.size:
                        sts	= (reply.status,reply.status_ext.data)
                yield ctx,reply,sts,val

    def harvest( self, issued, timeout=None ):
        """As we iterate over issued requests, collect the corresponding replies, match them up, and
        yield them as: (<index>,<descr>,<request>,<reply>,<status>,<value>).  We use the "lazy" zip
        to only collect responses as we need them.

        Invoke this directly with self.issue(...) to synchronously issue requests and collect their
        responses:
            tags		= [ "SCADA[1]=99", "SCADA[0-9]" ]
            operations		= parse_operations( tags )
            for idx,dsc,req,rpy,sts,val in cli.harvest( issued=cli.issue( operations, ... ))):
                ...

        Or, arrange for 'issued' to be a container (eg. list) which supports iteration and appending
        simultaneously, and then issue multiple requests before starting to harvest the results (see
        pipeline).

        Each response context and service code must match the request; this detects situations where
        (for example), the C*Logix responds to a Multiple Service Packet request with a general 0x1E
        error status to the entire Multiple Service Packet request, *not* individual responses; this 
        mismatch cannot be determined by the collect layer.

        """
        for (idx,req_ctx,dsc,op,req),col in zip(issued, self.collect( timeout=timeout )): # must be "lazy" zip!
            assert col, \
                "Request: %5d (Context: %10r/%10r) No Reply;\nop: %s\nrequest: %s\ncollected: %r via %r" % (
                    idx, req_ctx, None, parser.enip_format( op ), parser.enip_format( req ), col, self )
            (rpy_ctx,rpy,sts,val) = col
            assert rpy_ctx == req_ctx and rpy.service == req.service | 0x80, \
                "Request: %5d (Context: %10r/%10r) Mismatched;\nop: %s\nrequest: %s\nreply: %s" % (
                    idx, req_ctx, rpy_ctx, parser.enip_format( op ), parser.enip_format( req ), parser.enip_format( rpy ))
            yield idx,dsc,req,rpy,sts,val

    # 
    # synchronous
    # pipeline
    # 
    #     The normal APIs for issuing transactions and harvesting the corresponding results.
    # 
    #     The <value> yielded comes from the reply, hence there is a data list for reads, but no data
    # for writes (just a True).
    #
    #     None	-- Request failure
    #     True	-- Request successful write (no resultant data)
    #     [...]	-- Request successful read data
    # 
    #     Use validate to post-process these results, to fill in data for reads (from the request).
    # 
    def synchronous( self, operations, index=0, fragment=False, multiple=0, timeout=None ):
        """Issue the requested 'operations' synchronously.  Yield each harvested record.

        """
        for col in self.harvest(
                issued=self.issue(
                    operations=operations, index=index, fragment=fragment, multiple=multiple,
                    timeout=timeout ),
                timeout=timeout ):
            yield col

    def pipeline( self, operations, index=0, fragment=False, multiple=0, timeout=None, depth=1 ):
        """Issue the requested 'operations', allowing up to 'depth' outstanding requests to be in the
        pipeline, before beginning to harvest results.  Yield each harvested record.

        """
        class drainable( collections.deque ):
            """Use append() to add elements to the right; iterator drains from the left."""
            def __iter__( self ):
                return self
            def __next__( self ):
                try:
                    return self.popleft()
                except IndexError:
                    raise StopIteration
            next = __next__ # Python 2/3 compatibility
        
        issuer			= self.issue( operations=operations, index=index, fragment=fragment,
                                              multiple=multiple, timeout=timeout )
        inflight		= drainable()	# We iterate over this as we append to it...
        harvester		= self.harvest( issued=iter( inflight ), timeout=timeout )
        requests		= 0
        complete		= 0

        curr = last		= index - 1	# initial condition handles empty operations list
        while issuer or inflight:
            if issuer:
                try:
                    iss		= next( issuer )
                    curr	= iss[0]
                    requests   += 1
                    inflight.append( iss )
                    log.detail( "Issuing   %3d/%3d; curr: %3d - last: %3d == %3d depth vs. max %3d",
                                complete, requests, curr, last, curr - last, depth )
                except StopIteration:
                    issuer	= None
            if curr - last > depth or not issuer:
                try:
                    col		= next( harvester )
                    last	= col[0]
                    complete   += 1
                    log.detail( "Completed %3d/%3d; curr: %3d - last: %3d == %3d depth vs. max %3d",
                                complete, requests, curr, last, curr - last, depth )
                    yield col
                except StopIteration:
                    break
        log.detail( "Pipelined %3d/%3d; curr: %3d - last: %3d == %3d depth vs. max %3d",
                    complete, requests, curr, last, curr - last, depth )
        assert complete == requests, \
            "Communication ceased before harvesting all pipeline responses: %3d/%3d" % (
                complete, requests )

    def validate( self, harvested, printing=False ):
        """Iterate over the harvested (<index>,<descr>,<request>,<reply>,<status>,<value>) tuples, logging
        further details and (optionally) printing a summary to stdout if desired.  Each harvested
        record is re-yielded.

        For write_{tag,frag} requests, the incoming <value> will simply be Truthy (since the data
        array was sent in the request, and the response carried only a success/failure status).  In
        these cases, we fill in the <value> detail from the request before re-yielding harvested
        tuple (records for both reads and writes will therefore produce a data array for <value>).

        """
        for index,descr,request,reply,status,val in harvested:
            if log.isEnabledFor( logging.DETAIL ):
                log.detail( "Client %s Request: %s", descr, parser.enip_format( request ))
                log.detail( "  Yields Reply: %s", parser.enip_format( reply ))
            res			= None # result of request
            act			= "??" # denotation of request action; may be unrecognized (eg. service_code)
            try:
                if 'path' in request:
                    # Get a symbolic "Tag" or numeric "@<class>/<inst>/<attr>" into 'tag', and optional
                    # element into 'elm'.  Assumes the leading path.segment elements will be either
                    # 'symbolic' or 'class', 'instance', 'attribute', and the last may be 'element'.
                    tag		= format_path( request.path.segment )
                    elm		= None					# scalar access
                    if 'element' in request.path.segment[-1]:
                        elm		= request.path.segment[-1].element	# array access
                else:
                    tag		= 'Service Code 0x%02X%s' % (
                        request.service & 0x7f, ' Reply' if request.service & 0x80 else '' )
                    elm		= None

                # The response should contain either a status code (possibly with an extended
                # status), or the read_frag request's data.  Remember; a successful response may
                # carry read_frag.data, but report a status == 6 indicating that more data remains
                # to return via a subsequent fragmented read request.  Compute any Read/Write Tag
                # Fragmented 'off'-set, in elements (the Read request and the Write response
                # contains the offset and the data type).  Read Tag [Fragmented] replies won't
                # contain a '.read_tag'/'.read_frag' sub-dotdict (only a True) attribute if
                # reporting a failure status.
                off		= 0
                cnt		= 0
                if 'read_frag' in reply:
                    act		= "=="
                    if reply.status in (0x00, 0x06):
                        # Success (may be partial data); we don't try to compute actual element
                        # offset from byte offset, because of types (eg. [S]STRING) w/ indetermine len
                        off	= request.read_frag.get( 'offset', 0 )
                        cnt	= len( val )
                    else:
                        # Failure; no way to compute element offset requested, use count from request
                        cnt	= request.read_frag.get( 'elements', 0 )
                elif 'read_tag' in reply:
                    act		= "=="
                    off		= 0
                    cnt		= request.read_tag.get( 'elements', 0 )
                elif 'write_frag' in reply:
                    act		= "<="
                    off		= request.write_frag.get( 'offset', 0 )
                    val		= request.write_frag.data
                    cnt		= request.write_frag.elements - off
                elif 'write_tag' in reply:
                    act		= "<="
                    off		= 0
                    val		= request.write_tag.data
                    cnt		= request.write_tag.elements
                if not reply.status:
                    res		= "OK"
                else:
                    res		= "Status %d %s" % ( reply.status,
                        repr( reply.status_ext.data ) if 'status_ext' in reply and reply.status_ext.size else "" )
                if reply.status:
                    if not status:
                        status	= reply.status
                    log.warning( "Client %s returned non-zero status: %s", descr, res )

            except AttributeError as exc:
                res		= "Client %s Response missing data: %s" % ( descr, exc )
                log.normal( "%s: %s", res, ''.join( traceback.format_exception( *sys.exc_info() )))
                raise
            except Exception as exc:
                res		= "Client %s Exception: %s" % ( descr, exc )
                log.normal( "%s: %s", res, ''.join( traceback.format_exception( *sys.exc_info() )))
                raise

            if elm is None:
                line		= "%20s              %s %r: %r" % ( tag, act, val, res ) # scalar access
            else:
                line		= "%20s[%3d-%-3d]+%3d %s %r: %r" % ( tag, elm, elm + cnt - 1, off, act, val, res )
            log.normal( line )
            if printing:
                print( line )
            yield index,descr,request,reply,status,val

    # 
    #     Simplified interface wrappers; accepts all keyword parameters defined for synchronous/pipeline.
    # 
    # operate
    # 
    #     Select the appropriate combination of pipeline/synchronous, and validate, a yield all of
    # the operations' details.
    # 
    # results
    # process
    # 
    #     Simple, high-level API entry point that eliminates the need to process any yielded
    # sequences, and simply returns the number of (<failures>,<transactions>), optionally printing a
    # summary of I/O performed.
    # 
    def operate( self, operations, depth=0, printing=False, validating=False, **kwds ):
        """Operate on a sequence of I/O operations, yielding the details.  If a non-zero 'depth' is
        specified, then pipeline the requests allowing 'depth' outstanding transactions to be
        in-flight; otherwise, we just issue the transactions synchronously.

        If 'printing' or 'validating' is requested, uses self.validate to log/print a summary of I/O
        operations (and also fills in the yielded value written for successful Write Tag
        [Fragmented] requests, instead of just signalling success using True).

        Raises Exception on catastrophic failure of the connection.

        """
        if depth:
            harvested		= self.pipeline( operations=operations, depth=depth, **kwds )
        else:
            harvested		= self.synchronous( operations=operations, **kwds )
        if printing or validating:
            harvested		= self.validate( harvested=harvested, printing=printing )
        for idx,dsc,req,rpy,sts,val in harvested:
            yield idx,dsc,req,rpy,sts,val

    def results( self, operations, **kwds ):
        """Process a sequence of I/O operations, yielding just the results."""
        for idx,dsc,req,rpy,sts,val in self.operate( operations, **kwds ):
            yield val

    def process( self, operations, **kwds ):
        """Process a sequence of I/O operations, returning the a tuple (<failures>,[<result>,...]).
        Raises Exception on catastrophic failure of the connection.

        """
        transactions		= list( self.results( operations=operations, **kwds ))
        failures		= sum( 1 if t is None else 0 for t in transactions )
        return failures,transactions


class implicit( connector ):
    """Establishes an Implicit (Connected) EtherNet/IP CIP connection, by issuing a Forward Open after
    the EtherNet/IP CIP Register succeeds.

    Obtains defaults for any Forward Open parameters not specified, using the Object.config_loader,
    specialized for the given 'configuration' name (defaults to "Originator", if None, falling back
    to "DEFAULT" if not found).

    After successful establishment, the 'implicit' instance's 'self.established' attribute will
    contain the successful Forward Open response; 'self.requested' will contain the original forward
    Open request, and 'self.timeout' will contain the original timeout.  These will be used to issue
    the correct Forward Close request at the close of the session.

    While we typically issue a single Forward Open request on a connection, there is no reason that
    multiple Forward Open requests cannot be issued on a single EtherNet/IP session.  We'll track
    the O_T.connection_ID on each forward open, and create a sequence number for each Forward Open
    session, which subsequent calls to .connected_send( ..., connection=#, ... ) will use (it is
    expected that the O_T.connection_ID's for the desired supplied to identify the desired
    connection).

    A global sequence of connection_serial (used, by default, also as O_T.connection_ID is
    maintained.  This is unnecessarily strict, and there is nothing preventing independent Implicit
    connections from using the same O_T.connection_ID on different Forward Open sessions.
    Therefore, the connection-->sequence dict is maintained on a per-instance basis.

    """
    connection_serial		= random.randint( 0, 2**16-1 )
    def __init__( self, host, port=None, timeout=None, connection_path=None, path=None, 
                  configuration=None, priority_time_tick=None, timeout_ticks=None,
                  O_T=None, T_O=None, O_vendor=None, O_serial=None, connection_serial=None,
                  transport_class_triggers=None, connection_timeout_multiplier=None,
                  route_path=False, send_path='', # typically no 0x52 encapsulation w/ routing for fwd open
                  sender_context=b'', **kwds ):
        begun			= misc.timer()
        self.timeout		= timeout
        self.requested		= dotdict()
        self.established	= dotdict()
        self.seqs		= {} # Forward Open connected_send( connection --> sequence )

        super( implicit, self ).__init__( host=host, port=port, timeout=timeout,
                                          configuration=configuration, **kwds )

        # Substitute Connection_Manager for response parsing for duration of Forward Open
        dialect_bak,self.dialect= self.dialect,device.Connection_Manager
        try:
            assert not self.udp, "Cannot establish Implicit UDP EtherNet/IP CIP connections"
            self.__class__.connection_serial += 1
            self.__class__.connection_serial %= 2**16

            # Arrange to get the Forward Open parameters from the config file's 'configuration'
            # section, or from defaults.  The O_T/T_O Connection parameters must be obtained as a
            # package, as they must be internally consistent (ie. can't obtain some from config and
            # some from defaults)
            config			= device.Object.config_section( configuration )
            def default_named( val, name ):
                return device.Object.config_override(
                    val, name, defaults.forward_open_default.get( name ), config=config )
            path		= default_named( path,			'path' )
            connection_path	= default_named( connection_path,	'connection_path' )
            priority_time_tick	= default_named( priority_time_tick,	'priority_time_tick' ) 
            timeout_ticks	= default_named( timeout_ticks,		'timeout_ticks' )
            O_serial		= default_named( O_serial,		'O_serial' )
            O_vendor		= default_named( O_vendor,		'O_vendor' )
            T_O			= default_named( T_O,			'T_O' )
            O_T			= default_named( O_T,			'O_T' )
            transport_class_triggers \
                                = default_named( transport_class_triggers,'transport_class_triggers' )
            connection_timeout_multiplier \
                                = default_named( connection_timeout_multiplier, 'connection_timeout_multiplier' )

            # The RPI isn't strictly a connection parameter, but it's included in the same bundle;
            # get any configured/default values.
            T_O.RPI		= default_named( T_O.get( 'RPI' ),	'T_O.RPI' )
            O_T.RPI		= default_named( O_T.get( 'RPI' ),	'O_T.RPI' )

            # Deduce Connection parameters, and whether or not we need a Large or Small Forward Open
            T_O			= defaults.Connection( **( T_O or {} ))
            O_T			= defaults.Connection( **( O_T or {} ))
            T_O.large = O_T.large = O_T.large or T_O.large

            # Default the connection ID and serial to the same incrementing number
            if connection_serial is None:
                connection_serial = self.connection_serial
            if O_T.connection_ID is None:
                O_T.connection_ID = self.connection_serial
            if T_O.connection_ID is None:
                T_O.connection_ID = 2**32-1 # set by Target; doesn't matter

            with self:
                # The forward_open( timeout=... ) applies to the socket send only
                elapsed_req	= misc.timer() - begun
                self.requested	= self.forward_open(
                    path		= path,
                    connection_path	= connection_path,
                    priority_time_tick	= priority_time_tick,
                    timeout_ticks	= timeout_ticks,
                    O_serial		= O_serial,
                    O_vendor		= O_vendor,
                    connection_serial	= connection_serial,
                    O_T			= O_T.decoding,
                    T_O			= T_O.decoding,
                    transport_class_triggers = transport_class_triggers,
                    connection_timeout_multiplier = connection_timeout_multiplier,
                    timeout		= None if timeout is None else max( 0, timeout - elapsed_req ),
                    route_path		= route_path,
                    send_path		= send_path,
                    sender_context	= sender_context )

                # Await the CIP response for remainder of timeout
                elapsed_req	= misc.timer() - begun
                data,elapsed_rpy= await_response( self, timeout=None if timeout is None else max( 0, timeout - elapsed_req ))

            assert data is not None, "Failed to receive any response"
            assert 'enip.status' in data, "Failed to receive EtherNet/IP response"
            assert data.enip.status == 0, "EtherNet/IP response indicates failure: %s" % data.enip.status
            self.established		= data.get( 'enip.CIP.send_data.CPF.item[1].unconnected_send.request' )
            assert self.established and 'forward_open' in self.established and self.established.status == 0, \
                "Failed to receive successful Forward Open response: %s" % ( parser.enip_format( self.established ))
        except Exception as exc:
            log.info( "FwdOpen:  Failure in %7.3f/%7.3fs: %s", misc.timer() - begun,
                      misc.inf if timeout is None else timeout, exc )
            raise
        else:
            log.detail( "FwdOpen:  Success in %7.3f/%7.3fs", misc.timer() - begun,
                        misc.inf if timeout is None else timeout )
        finally:
            self.dialect	= dialect_bak # Restore original self.dialect

    def close( self ):
        """Attempt to cleanly close the Implicit Forward Opened connection by sending a corresponding
        Forward Close, followed immediately by a shutdown the socket.  If it fails, capture and log
        the failure, but continue with the close, as this is often executed as part of the
        destruction of a connection.  We will use the values returned in the Forward Open response
        saved in self.established, and the original connection_path, etc. saved in self.requested.

        Since we can't have a constructed object unless the original Forward Open succeeded, we can
        assume that we must perform the Forward Close; actually, there are -- __del__ (and hence
        .close()) is invoked on partially constructed objects.

        If the socket has already been closed, this will fail immediately with a socket.error EPIPE.
        In general, the caller may want to ignore failures due to socket errors on closing; if the
        Python object is allowed to be destructed normally, exceptions raised during __del__
        invocation are ignored.  However, if you invoke close directly, be prepared to handle an
        Exception in the (likely) case that the socket has already closed.

        """
        begun			= misc.timer()
        dialect_bak,self.dialect= getattr( self, 'dialect', None ),device.Connection_Manager
        try:
            if not hasattr( self, 'established' ):
                return
            if 'forward_open' not in self.established or self.established.status != 0:
                if log.isEnabledFor( logging.INFO ):
                    log.info( "No Forward Open; not executing Forward Close: %s", parser.enip_format( self.established ))
                return
            if log.isEnabledFor( logging.INFO ):
                log.info( "Forward Close w/ \nRequested: %s, \nEstablished: %s",
                            parser.enip_format( self.requested ), parser.enip_format( self.established ))
            with self:
                self.forward_close(
                    path		= self.requested.path.segment,
                    connection_path	= self.requested.forward_open.connection_path.segment,
                    timeout_ticks	= self.requested.forward_open.timeout_ticks,
                    priority_time_tick	= self.requested.forward_open.priority_time_tick,
                    O_serial		= self.established.forward_open.O_serial,
                    O_vendor		= self.established.forward_open.O_vendor,
                    connection_serial	= self.established.forward_open.connection_serial )
                self.shutdown()
                # Await the CIP response for remainder of self.timeout
                elapsed_req	= misc.timer() - begun
                data,elapsed_rpy= await_response( self, timeout=None if self.timeout is None else max( 0, self.timeout - elapsed_req ))
            replies		= enip_replies( data ) 
            if data is None: # [<replies>], None or {} (EOF), or Exception/ENIPStatusError
                # Response to Forward Close + socket shutdown was ... silence.  This connection is no good.
                raise Exception( "Failed to cleanly close Implicit (Connected) session after %7.3f/%7.3fs" % (
                    misc.timer() - begun, misc.inf if self.timeout is None else self.timeout ))
            # Either {} (EOF), or a forward_close response { 'enip':... }
            assert not replies or len( replies ) == 1 and 'forward_close' in replies[0], \
                "Failed to receive successful Forward Close response: %s" % ( parser.enip_format( data ))
        except Exception as exc:
            log.detail( "FwdClose: Failure in %7.3f/%7.3fs: %s", misc.timer() - begun,
                        misc.inf if self.timeout is None else self.timeout, exc )
            raise
        else:
            log.detail( "FwdClose: Success in %7.3f/%7.3fs", misc.timer() - begun,
                        misc.inf if self.timeout is None else self.timeout )
        finally:
            self.dialect	= dialect_bak # Restore original self.dialect
            super( implicit, self ).close()

    def index_to_sender_context( self, _index ):
        """Disappointingly, C*Logix PLCs do *not* respond with the supplied Sender Context..."""
        return b''

    def connected_send( self, request,
                        connection=None, sequence=None, **kwds ):
        """If connection and/or sequence not supplied default to the established Forward Open
        O_T_connection_ID, and/or the next sequence number for the O_T_connection_ID (starting w/
        sequence == 0 for each connection).

        """
        if connection is None:
            connection		= self.established.forward_open.O_T.connection_ID
        if sequence is None: # advance sequence, ensuring it remains in valid CIP INT range (0,2^16]
            sequence		= self.seqs.get( connection, -1 ) + 1 # 0, 1, ...
            sequence	       %= 2**16
            self.seqs[connection] = sequence
        return super( implicit, self ).connected_send(
            request, connection=connection, sequence=sequence, **kwds )

    def req_send( self, request, route_path=None, send_path=None, **kwds ):
        """Sending a request on a client connector/implicit connection requires the use of the appropriate
        encapsulation.  An implicit connection normally uses a connected_send "Send Unit Data".
        Normally, we'll deduce the 'connection' and 'sequence' in connected_send.

        However, we *can* send an arbitrarily routed request (ie. one with a route_path and/or send_path)
        via an implicit connection, with SendRRData encapsulation.
        """
        if route_path or send_path:
            return super( implicit, self ).req_send(
                request, route_path=route_path, send_path=send_path, **kwds )
        else:
            return self.connected_send( request, **kwds )


def recycle( iterable, times=None ):
    """Record and repeat an iterable x 'times'; forever if times is None (the default), not at all if
    times is 0.  Like itertools.cycle, but with an optional 'times' limit.

    """
    assert times is None or ( times // 1 == times and times >= 0 ), \
        "Invalid cycle 'times'; must be None or +'ve integer: %r" % ( times )
    saved			= []
    if times == 0:
        return
    for element in iterable:
        yield element
        saved.append( element )

    while times != 1:
        for element in saved:
              yield element
        if times is not None:
            times	       -= 1


def main( argv=None ):
    """Read/write the specified tag(s) silently (by default); pass --print to summarize transaction to
    standard output.  Pass the desired argv (excluding the program name in sys.arg[0]; typically
    pass argv=None, which is equivalent to argv=sys.argv[1:], the default for argparse.

    """
    ap				= argparse.ArgumentParser(
        description = "An EtherNet/IP Client",
        formatter_class = argparse.RawDescriptionHelpFormatter,
        epilog = """\

One or more EtherNet/IP CIP Tags or Object/Instance Attributes may be read or
written.  The full format for specifying a tag and an operation is:

    Tag[<first>-<last>]+<offset>=(SINT|INT|DINT|REAL)<value>,<value>

All components except Tag are optional.  Specifying a +<offset> (in bytes)
forces the use of the Fragmented command, regardless of whether --[no-]fragment
was specified.  If an element range [<first>] or [<first>-<last>] was specified
and --no-fragment selected, then the exact correct number of elements must be
provided.

The default Send Path is '@6/1', and the default Route Path is [{"link": 0,
"port":1}].  This should work with a device that can route requests to links
(eg. a *Logix Controller), with the Processor is slot 1 of the chassis.  If you
have a simpler device (ie. something that does not route requests, such as an AB
PowerFlex for example), then you may want to specify:

    --send-path='' --route-path=false

to eliminate the *Logix-style Unconnected Send (service 0x52) encapsulation
which is required to carry this Send/Route Path data. """ )

    ap.add_argument( '-v', '--verbose',
                     default=0, action="count",
                     help="Display logging information." )
    ap.add_argument( '-a', '--address',
                     default=( "%s:%d" % defaults.address ),
                     help="EtherNet/IP interface[:port] to connect to (default: %s:%d)" % (
                         defaults.address[0] or 'localhost', defaults.address[1] or 44818 ))
    ap.add_argument( '-u', '--udp', action='store_true',
                     default=False, 
                     help="Use a UDP/IP connection (default: False)" )
    ap.add_argument( '-b', '--broadcast', action='store_true',
                     default=False, 
                     help="Allow multiple peers, and use of broadcast address (default: False)" )
    ap.add_argument( '-p', '--print', action='store_true',
                     default=False, # inconsistent default from get_attribute.py, for historical reasons
                     help="Print a summary of operations to stdout (default: False)" )
    ap.add_argument( '--no-print', action='store_false', dest='print',
                     help="Disable printing of summary of operations to stdout" )
    ap.add_argument( '-l', '--log',
                     help="Log file, if desired" )
    ap.add_argument( '-t', '--timeout',
                     default=5.0,
                     help="EtherNet/IP timeout (default: 5s)" )
    ap.add_argument( '-r', '--repeat',
                     default=1,
                     help="Repeat EtherNet/IP request (default: 1)" )
    ap.add_argument( '--route-path',
                     default=None,
                     help="Route Path, as <port>/<link> or JSON (default: %r); 0/false to specify no/empty route_path" % (
                         str( json.dumps( connector.route_path_default ))))
    ap.add_argument( '--send-path',
                     default=None,
                     help="Send Path to UCMM (default: @6/1); Specify an empty string '' for no Send Path" )
    ap.add_argument( '--priority-time-tick',
                     default=None,
                     help="Timeout tick length N range (0,15) (default: %s == %sms), where each tick is 2**N ms. Eg. 0 ==> 1ms., 5 ==> 32ms., 15 ==> 32768ms." % (
                         defaults.priority_time_tick, 2 ** defaults.priority_time_tick ))
    ap.add_argument( '--timeout-ticks',
                     default=None,
                     help="Timeout duration ticks in range (1,255) (default: %s == %sms)" % (
                         defaults.timeout_ticks, defaults.timeout_ticks * ( 2 ** defaults.priority_time_tick )))
    ap.add_argument( '-S', '--simple', action='store_true',
                     default=False,
                     help="Access a simple (non-routing) EtherNet/IP CIP device (eg. MicroLogix)")
    ap.add_argument( '-m', '--multiple', action='store_true',
                     default=False, 
                     help="Use Multiple Service Packet request targeting ~500 bytes (default: False)" )
    ap.add_argument( '-d', '--depth', default=1,
                     help="Pipeline requests to this depth (default: 1)" )
    ap.add_argument( '-f', '--fragment', dest='fragment', action='store_true',
                     default=False,
                     help="Always use Read/Write Tag Fragmented requests (default: False)" )
    ap.add_argument( '-s', '--list-services', action='store_true',
                     default=False,
                     help="Perform a CIP List Services request upon connection (default: False)" )
    ap.add_argument( '-i', '--list-identity', action='store_true',
                     default=False,
                     help="Perform a CIP List Identity request upon connection (default: False)" )
    ap.add_argument( '-I', '--list-interfaces', action='store_true',
                     default=False,
                     help="Perform a CIP List Interfaces request upon connection (default: False)" )
    ap.add_argument( '-L', '--legacy',
                     default=None,
                     help="Send a Legacy CIP request (specify command code) (default: None)" )
    ap.add_argument( '-P', '--profile', action='store_true',
                     default=False, 
                     help="Activate profiling (default: False)" )
    ap.add_argument( '-c', '--connected', action='store_true',
                     default=False,
                     help="Establish a Connected (Implicit) Session (uses configured/default parameters")
    ap.add_argument( 'tags', nargs="*",
                     help="Tags to read/write (- to read from stdin), eg: SCADA[1], SCADA[2-10]+4=(DINT)3,4,5" )
    args			= ap.parse_args( argv )

    # Set up logging level (-v...) and --log <file>
    levelmap 			= {
        0: logging.WARNING,
        1: logging.NORMAL,
        2: logging.DETAIL,
        3: logging.INFO,
        4: logging.DEBUG,
        }
    log_cfg['level']		= ( levelmap[args.verbose] 
                                    if args.verbose in levelmap
                                    else logging.DEBUG )
    if args.log:
        log_cfg['filename'] = args.log

    logging.basicConfig( **log_cfg )

    addr			= args.address.split( ':', 1 )
    assert 1 <= len( addr ) <= 2, "Invalid --address [<interface>][:<port>]: %s" % args.address
    addr			= ( str( addr[0] ) if addr[0] else defaults.address[0],
                                    int( addr[1] ) if len( addr ) > 1 and addr[1] else defaults.address[1] )
    timeout			= float( args.timeout )
    repeat			= int( args.repeat )
    depth			= int( args.depth )
    multiple			= 500 if args.multiple else 0
    fragment			= bool( args.fragment )
    printing			= args.print
    # route_path may be None/0/False/'[]', send_path may be None/''/'@2/1'.  -S|--simple designates
    # '[]', '' respectively, appropriate for non-routing CIP devices, eg. MicroLogix, PowerFlex, ...
    route_path			= args.route_path if args.route_path \
                                      else [] if args.simple else None
    send_path			= args.send_path if args.send_path \
                                      else '' if args.simple else None
    priority_time_tick		= None if args.priority_time_tick is None \
                                      else int( args.priority_time_tick )
    timeout_ticks		= None if args.timeout_ticks is None \
                                      else int( args.timeout_ticks )
    if '-' in args.tags:
        # Collect tags from sys.stdin 'til EOF, at position of '-' in argument list
        minus			= args.tags.index( '-' )
        tags			= itertools.chain( args.tags[:minus], sys.stdin, args.tags[minus+1:] )
    else:
        tags			= args.tags

    profiler			= None
    if args.profile:
        import cProfile as profile
        import pstats
        import StringIO
        profiler		= profile.Profile()

    # Register and EtherNet/IP CIP connection to a Controller; default to Explicit, but support Implicit
    begun			= misc.timer()
    failures			= 0
    connector_cls		= connector
    connector_kwds		= {}
    if args.connected:
        connector_cls		= implicit
    with connector_cls( host=addr[0], port=addr[1], timeout=timeout, profiler=profiler,
                        udp=args.udp, broadcast=args.broadcast, **connector_kwds ) as connection:
        elapsed			= misc.timer() - begun
        log.detail( "Client Register Rcvd %7.3f/%7.3fs" % ( elapsed, timeout ))

        # Issue List {Identity,Service} requests, if desired.  If broadcast, await (multiple)
        # responses for the entire timeout.  Prints the CPF encapsulation payload of each response
        # (if available; the entire parsed EtherNet/IP reply if not recognized).
        for desc in [ "Legacy", "List Services", "List Identity", "List Interfaces" ]:
            meth		= desc.lower().replace( ' ', '_' ) # List Interfaces --> list_interfaces
            if not getattr( args, meth, None ):
                continue # not selected, or no arg option yet, or no/zero --legacy command value

            path		= '.'.join( [ 'enip', 'CIP', meth, 'CPF' ] )
            begun		= misc.timer()
            meth_kwds		= dict( timeout=timeout )
            if desc == "Legacy":
                # All legacy EtherNet/IP commands require a command value, and an empty 'CIP.legacy'
                # payload to be passed to client.legacy/client.cip_send (command cannot be deduced)
                command		= int( args.legacy, 0 ) # may be hex, eg. '0x0001'
                desc	       += " 0x%04X" % ( command )
                meth_kwds.update(
                    command	= command,
                    cip		= dotdict(
                        legacy	= None ))

            getattr( connection, meth )( **meth_kwds )
            elapsed		= None
            counter		= 0
            while ( elapsed is None or elapsed < timeout ):
                remains		= timeout - ( elapsed or 0 )
                reply,_		= await_response( connection, timeout=remains )
                if reply:
                    print( "%s %2d from %r: %s" % (
                        desc, counter, reply.peer, parser.enip_format( reply.get( path, reply ))))
                    counter    += 1
                if not reply or not args.broadcast:
                    # No reply or EOF w'in timeout, or reply but not --broadcast; done waiting
                    break
                elapsed		= misc.timer() - begun
            if not counter:
                log.warning( "No %s response w/in %7.3fs timeout", desc, timeout )
                failures       += 1

        if tags:
            # Issue Tag I/O operations, optionally printing a summary
            begun		= misc.timer()
            operations		= parse_operations(
                recycle( tags, times=repeat ), route_path=route_path, send_path=send_path,
                timeout_ticks=timeout_ticks, priority_time_tick=priority_time_tick )
            failed,transactions	= connection.process(
                operations=operations, depth=depth, multiple=multiple,
                fragment=fragment, printing=printing, timeout=timeout )
            failures	       += failed
            elapsed		= misc.timer() - begun
            if transactions: # May be [], if from stdin, and no operations provided
                log.normal( "Client Tag I/O  Average %7.3f TPS (%7.3fs ea)." % (
                    len( transactions ) / elapsed, elapsed / len( transactions )))

    if profiler:
        s			= StringIO.StringIO()
        ps			= pstats.Stats( profiler, stream=s )
        for sortby in [ 'cumulative', 'time' ]:
            ps.sort_stats( sortby )
            ps.print_stats( 25 )
        print( s.getvalue() )

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit( main() )
