# Python Data Serialization and Embedded Databases Benchmarks

## Python Data Serialization Libraries
- Pickle: with dict message types
- ujson
- shelve
- orjson: with dict message types
- [MessagePack](https://msgpack.org/index.html)
- [Quickle](https://jcristharif.com/quickle/index.html)
- parquet
- feather

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

### Data Structure:
List of 1M of dicts
