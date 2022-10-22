# Python Data Benchmarks

### Data Structure:
List of 1M of key values, with different types of values: int, float, strings

## Python Data Objects
Metrics: size, single index, range index, filtering, groupby, pivot_table
- dict of dicts
- list of dicts
- list of tuples
- list of lists
- list of objects
- list of numpy arrays
- dict of numpy arrays
- dict of key names and numpy Nd array
- Pandas
- Polars

## Python Data Persistence:
Metrics: file size, save time, load time
- Pickle: with dict message types
- ujson
- shelve
- orjson: with dict message types
- [MessagePack](https://msgpack.org/index.html)
- [Quickle](https://jcristharif.com/quickle/index.html)
- parquet
- feather
- arrow

## Python Embedded Databases
https://charlesleifer.com/blog/completely-un-scientific-benchmarks-of-some-embedded-databases-with-python/

- PickleDB
- TinyDB
- HDF5
- ZODB
- UnQLite: unqlite-python (ctypes)
- Vedis: vedis-python (ctypes)
- GDBM: standard library (C)
- BerkeleyDB (b-tree and hash-table): bsddb3 (C)
- KyotoCabinet (b-tree and hash-table): kyotocabinet (C++)
- LevelDB: plyvel (Cython)
- RocksDB: pyrocksdb (Cython)
- SQLite: standard library (C and Python)

## Python Mem-Cache DB
- Sqlite3
- DiskCache
- Memcached
- Redis
